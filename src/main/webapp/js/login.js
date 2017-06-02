function login() {

var email = document.formulario.email.value;
var pass = document.formulario.password.value;

  const auth = firebase.auth();

auth.signInWithEmailAndPassword(email, pass);
}
