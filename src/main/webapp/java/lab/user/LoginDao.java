package lab.user;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.persistence.TypedQuery;

/**
 * Data Access Object.
 */
public class LoginDao {

	private static EntityManagerFactory emf = Persistence.createEntityManagerFactory("lab-persistence-unit");

	public static void inclui(String email, String senha) {
		// Obter "conexão".
		EntityManager em = emf.createEntityManager();
		em.getTransaction().begin();

		Login login = new Login();
		login.setEmail(email);
		login.setSenha(senha);

		// Grava o objeto no banco de dados.
		em.persist(login);
		em.getTransaction().commit();
		em.close();
	}

	public static void alterar(String email, String senha) {
	}

	public static void excluir(String email) {
	}

}
