from flask import Flask
from src.routes import detalle_venta_routes, ingrediente_routes, marca_routes, permiso_routes, produccion_routes, producto_routes, receta_ingrediente_routes, receta_routes, rol_routes, tipo_documento_routes, unidad_medida_routes, usuario_routes, ventas_routes, pages_routes

app = Flask(__name__)

def init_app(config):
    # PASAMOS LA CONFIGURACION
    app.config.from_object(config)
    # ESPACIO PARA RUTAS
    app.register_blueprint(detalle_venta_routes.detalle_venta, url_prefix='/detalles_ventas')
    app.register_blueprint(ingrediente_routes.ingrediente, url_prefix='/ingredientes')
    app.register_blueprint(marca_routes.marca, url_prefix='/marcas')
    app.register_blueprint(permiso_routes.permiso, url_prefix='/permisos')
    app.register_blueprint(produccion_routes.produccion, url_prefix='/producciones')
    app.register_blueprint(producto_routes.producto, url_prefix='/productos')
    app.register_blueprint(receta_ingrediente_routes.receta_ingrediente, url_prefix='/recetas_ingredientes')
    app.register_blueprint(receta_routes.receta, url_prefix='/recetas')
    app.register_blueprint(rol_routes.rol, url_prefix='/roles')
    app.register_blueprint(tipo_documento_routes.tipo_documento, url_prefix='/tipos_documentos')
    app.register_blueprint(unidad_medida_routes.unidad_medida, url_prefix='/unidades_medidas')
    app.register_blueprint(usuario_routes.usuario, url_prefix='/usuarios')
    app.register_blueprint(ventas_routes.venta, url_prefix='/ventas')
    app.register_blueprint(pages_routes.page, url_prefix='/')

    return app