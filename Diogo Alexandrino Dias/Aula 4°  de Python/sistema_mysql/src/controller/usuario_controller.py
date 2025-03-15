from ..model.usuario_model import usuariomodel

def listar_usuarios():
    USmodel = usuariomodel()
    usuarios = USmodel.get_all_user()
    USmodel.close_connection_user()
    return usuarios

def cadastrar_usuario(usuario_nome,idade):
    """ Cadastras produtos no banco """
    USmodel = usuariomodel()
    US_novo_id = USmodel.insert_user(usuario_nome,idade)
    USmodel.close_connection_user()
    return US_novo_id
    
def atualizar_usuario(usuario_id,usuario_nome,idade):
    USmodel = usuariomodel()
    US_linhas_afetadas = USmodel.update_user_by_id(usuario_id,usuario_nome,idade)
    USmodel.close_connection_user()
    return US_linhas_afetadas

def remover_usuario(usuario_id):
    USmodel = usuariomodel()
    US_linha_afetadas = USmodel.delete_user_by_id(usuario_id)
    USmodel.close_connection_user()
    return US_linha_afetadas

def obter_ususario(usuario_id):
    USmodel = usuariomodel()
    usuario = USmodel.get_user_by_id(usuario_id)
    USmodel.close_connection_user()
    return usuario








      




