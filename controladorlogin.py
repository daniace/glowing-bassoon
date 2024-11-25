from ABMSprueba.modelologin import ModeloLogin
from ABMSprueba.vistalogin import VistaLogin
from ABMSprueba.vistaprincipal import VistaPrincipal


class ControladorLogin:
    def __init__(self):
        self.modelo = ModeloLogin()
        self.vista = VistaLogin()
        self.vista.conectar_boton_login(self.validar_login)

    def validar_login(self):
        """Valida las credenciales ingresadas."""
        username, password = self.vista.obtener_credenciales()
        if self.modelo.validar_usuario(username, password):
            self.vista.mostrar_resultado("Login exitoso")
            self.abrir_ventana_principal()
        else:
            self.vista.mostrar_resultado("Login fallido")

    def abrir_ventana_principal(self):
        """Abre la ventana principal con los tres botones."""
        self.close()
        vista_principal = VistaPrincipal()
        vista_principal.iniciar()

    def run(self):
        """Inicia la aplicación."""
        self.visible = True
        self.vista.iniciar()

    def close(self):
        """Cierra la ventana de la vista."""
        self.vista.cerrar()


if __name__ == "__main__":
    app = ControladorLogin()
    app.run()
