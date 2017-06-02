function signup() {

  var email = document.formulario.email.value;
  var pass = document.formulario.password.value;

  const auth = firebase.auth()

  auth.createUserWithEmailAndPassword(email, pass)
}
