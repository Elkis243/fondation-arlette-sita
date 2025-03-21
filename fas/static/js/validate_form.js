document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#customValidationForm');
  const inputs = form.querySelectorAll('input, textarea, select');

  form.addEventListener('submit', (event) => {
      let isValid = true;

      inputs.forEach((input) => {
          if (!input.checkValidity()) {
              isValid = false;
              validateField(input);
          }
      });
      if (!isValid) {
          event.preventDefault();
          event.stopPropagation();
          form.classList.add('was-validated');
          
      }
  });

  inputs.forEach((input) => {
      input.addEventListener('input', () => validateField(input));
      input.addEventListener('blur', () => validateField(input));
  });

  function validateField(field) {
      let feedback = field.nextElementSibling;

      if (!feedback) return;

      if (feedback && field.validity.valid) {
          field.classList.remove("is-invalid");
          field.classList.add("is-valid");
          feedback.textContent = '';
      } else {
          field.classList.remove("is-valid");
          field.classList.add("is-invalid");

          if (field.validity.valueMissing) {
              feedback.textContent = `Ce champ ne peut pas être laissé vide !`;
          } else if (field.validity.tooShort) {
              feedback.textContent = `Ce champ doit contenir au moins ${field.minLength || 0} caractères !`;
          } else if (field.validity.tooLong) {
              feedback.textContent = `Ce champ ne doit pas dépasser ${field.maxLength || 0} caractères !`;
          } else if (field.validity.patternMismatch) {
              feedback.textContent = `Veuillez respecter le format requis pour ce champ !`;
          } else if (field.type === 'radio' && !isRadioGroupValid(field)) {
              feedback.textContent = `Ce champ ne peut pas être laissé vide !`;
          } else if (field.type === 'checkbox' && !isCheckboxValid(field)) {
              feedback.textContent = `Ce champ ne peut pas être laissé vide !`;
          } else {
              feedback.textContent = `Ce champ est invalide !`;
          }
      }
  }

  function isRadioGroupValid(radio) {
      const radioGroup = document.querySelectorAll(`input[name="${radio.name}"]`);
      return Array.from(radioGroup).some(radio => radio.checked);
  }

  function isCheckboxValid(checkbox) {
      return checkbox.checked;
  }
});
