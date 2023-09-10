class Usuario:

    def __init__(self, id_usuario, id_rol, id_tipo_documento, password_usuario, doc_usuario, nombres_usuario, apellidos_usuario, telefono_usuario, email_usuario, estado_rg, fecha_rg, fecha_md) -> None:
        self.id_usuario = id_usuario
        self.id_rol = id_rol
        self.id_tipo_documento = id_tipo_documento
        self.password_usuario = password_usuario
        self.doc_usuario = doc_usuario
        self.nombres_usuario = nombres_usuario
        self.apellidos_usuario = apellidos_usuario
        self.telefono_usuario = telefono_usuario
        self.email_usuario = email_usuario
        self.estado_rg = estado_rg
        self.fecha_rg = fecha_rg
        self.fecha_md = fecha_md