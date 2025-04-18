// Exécution une fois que le DOM est entièrement chargé
document.addEventListener('DOMContentLoaded', () => {

  // Sélection du formulaire de réinitialisation de mot de passe
  const form = document.querySelector('#customPasswordResetForm');

  // Sélection des deux champs de mot de passe
  const new_password1 = document.querySelector('#new_password1');
  const new_password2 = document.querySelector('#new_password2');

  // Événement sur la soumission du formulaire
  form.addEventListener('submit', (event) => {
    let isValid = true;

    // Validation des champs (ordre important)
    isValid = checkFieldIsNotEmpty(new_password1) && isValid;  // Vérifie que le champ 1 n'est pas vide
    isValid = checkFieldIsNotEmpty(new_password2) && isValid;  // Vérifie que le champ 2 n'est pas vide
    isValid = validatePasswordLength(new_password1) && isValid; // Vérifie la longueur du mot de passe
    isValid = validatePasswordMatch(new_password1, new_password2) && isValid; // Vérifie que les mots de passe sont identiques

    // Si une erreur est détectée, on empêche l'envoi du formulaire
    if (!isValid) {
      event.preventDefault();
      event.stopPropagation();
    }
  });

  // Feedback en temps réel pendant la saisie
  new_password1.addEventListener('input', () => {
    checkFieldIsNotEmpty(new_password1);
    validatePasswordLength(new_password1);
    validatePasswordMatch(new_password1, new_password2);
  });

  new_password2.addEventListener('input', () => {
    checkFieldIsNotEmpty(new_password2);
    validatePasswordMatch(new_password1, new_password2);
  });

  // Feedback lorsque l'utilisateur quitte un champ
  new_password1.addEventListener('blur', () => {
    checkFieldIsNotEmpty(new_password1);
    validatePasswordLength(new_password1);
    validatePasswordMatch(new_password1, new_password2);
  });

  new_password2.addEventListener('blur', () => {
    checkFieldIsNotEmpty(new_password2);
    validatePasswordMatch(new_password1, new_password2);
  });

  // ===== Fonctions de validation =====

  /**
   * Vérifie qu’un champ n’est pas vide.
   * Affiche un message d’erreur si nécessaire.
   */
  function checkFieldIsNotEmpty(field) {
    let feedback = field.nextElementSibling;
    let isValid = true;

    if (!field.value.trim()) {
      isValid = false;
      setFieldInvalid(field, feedback, `Ce champ ne peut pas être laissé vide !`);
    } else {
      setFieldValid(field, feedback);
    }

    return isValid;
  }

  /**
   * Vérifie que le mot de passe a une longueur acceptable (entre 8 et 20 caractères).
   */
  function validatePasswordLength(field) {
    let feedback = field.nextElementSibling;
    let isValid = true;

    // Si vide, ne continue pas la validation
    if (!field.value.trim()) {
      return false;
    }

    const length = field.value.length;

    if (length < 8) {
      isValid = false;
      setFieldInvalid(field, feedback, `Le mot de passe doit contenir au moins 8 caractères !`);
    } else if (length > 20) {
      isValid = false;
      setFieldInvalid(field, feedback, `Le mot de passe ne doit pas dépasser 20 caractères !`);
    } else {
      setFieldValid(field, feedback);
    }

    return isValid;
  }

  /**
   * Vérifie que les deux champs de mot de passe sont identiques.
   */
  function validatePasswordMatch(field1, field2) {
    let feedback = field2.nextElementSibling;
    let isValid = true;

    if (field1.value && field2.value && field1.value !== field2.value) {
      isValid = false;
      setFieldInvalid(field2, feedback, `Les mots de passe ne correspondent pas !`);
    } else if (field2.value) {
      setFieldValid(field2, feedback);
    }

    return isValid;
  }

  // ===== Fonctions utilitaires =====

  /**
   * Marque un champ comme valide (visuellement) et efface le message d'erreur.
   */
  function setFieldValid(field, feedback) {
    field.classList.remove("is-invalid");
    field.classList.add("is-valid");
    feedback.textContent = '';
  }

  /**
   * Marque un champ comme invalide (visuellement) et affiche un message d'erreur.
   */
  function setFieldInvalid(field, feedback, message) {
    field.classList.remove("is-valid");
    field.classList.add("is-invalid");
    feedback.textContent = message;
  }

});
