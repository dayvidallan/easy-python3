# coding: utf-8

from django.conf.urls import url
from base import views
from base.views import SecretariaAutocomplete, ParticipantePregaoAutocomplete, PessoaFisicaAutocomplete, MaterialConsumoAutocomplete, PregaoView, ARPView, \
    FornecedorAutocomplete

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^solicitacoes/$', views.solicitacoes, name='solicitacoes'),
    url(r'^cadastros/$', views.cadastros, name='cadastros'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^busca_pessoa/$', views.busca_pessoa, name='busca_pessoa'),
    url(r'^gestao_pedidos_tipo/$', views.gestao_pedidos_tipo, name='gestao_pedidos_tipo'),
    url(r'^solicitacoes_do_setor/$', views.solicitacoes_do_setor, name='solicitacoes_do_setor'),
    url(r'^outras_solicitacoes/$', views.outras_solicitacoes, name='outras_solicitacoes'),
    url(r'^busca_tipo_pregao/$', views.busca_tipo_pregao, name='busca_tipo_pregao'),
    url(r'^lista_fornecedores/$', views.lista_fornecedores, name='lista_fornecedores'),
    url(r'^relatorio_auditoria/$', views.relatorio_auditoria, name='relatorio_auditoria'),
    url(r'^portal_transparencia/$', views.portal_transparencia, name='portal_transparencia'),
    url(r'^baixar_licitacoes_portal/$', views.baixar_licitacoes_portal, name='baixar_licitacoes_portal'),
    url(r'^baixar_atas_portal/$', views.baixar_atas_portal, name='baixar_atas_portal'),
    url(r'^baixar_contratos_portal/$', views.baixar_contratos_portal, name='baixar_contratos_portal'),
    url(r'^baixar_dispensas_portal/$', views.baixar_dispensas_portal, name='baixar_dispensas_portal'),
    url(r'^baixar_adesao_atas_portal/$', views.baixar_adesao_atas_portal, name='baixar_adesao_atas_portal'),


    url(r'^modelos_atas/(?P<pregao_id>\d+)/$', views.modelos_atas, name='modelos_atas'),
    url(r'^modelos_documentos/$', views.modelos_documentos, name='modelos_documentos'),
    url(r'^cadastrar_modelo_documento/$', views.cadastrar_modelo_documento, name='cadastrar_modelo_documento'),
    url(r'^editar_modelo_documento/(?P<documento_id>\d+)/$', views.editar_modelo_documento, name='editar_modelo_documento'),
    url(r'^deletar_modelo_documento/(?P<documento_id>\d+)/$', views.deletar_modelo_documento, name='deletar_modelo_documento'),

    url(r'^cadastrar_modelo_ata/(?P<pregao_id>\d+)/$', views.cadastrar_modelo_ata, name='cadastrar_modelo_ata'),
    url(r'^editar_modelo_ata/(?P<ata_id>\d+)/(?P<pregao_id>\d+)/$', views.editar_modelo_ata, name='editar_modelo_ata'),
    url(r'^deletar_modelo_ata/(?P<ata_id>\d+)/(?P<pregao_id>\d+)/$', views.deletar_modelo_ata, name='deletar_modelo_ata'),
    url(r'^ata_sessao_outras_modalidades/(?P<pregao_id>\d+)/$', views.ata_sessao_outras_modalidades, name='ata_sessao_outras_modalidades'),


    url(r'^administracao/$', views.administracao, name='administracao'),
    url(r'^auditoria/$', views.auditoria, name='auditoria'),
    url(r'^pregao/(?P<pregao_id>\d+)/$', views.pregao, name='pregao'),
    url(r'^itens_solicitacao/(?P<solicitacao_id>\d+)/$', views.itens_solicitacao, name='itens_solicitacao'),
    url(r'^rejeitar_informar_quantidades/(?P<solicitacao_id>\d+)/(?P<secretaria_id>\d+)/$', views.rejeitar_informar_quantidades, name='rejeitar_informar_quantidades'),

    url(r'^planilha_propostas_solicitacao/(?P<solicitacao_id>\d+)/$', views.planilha_propostas_solicitacao, name='planilha_propostas_solicitacao'),


    url(r'^cadastrar_item_solicitacao/(?P<solicitacao_id>\d+)/$', views.cadastrar_item_solicitacao, name='cadastrar_item_solicitacao'),
    url(r'^cadastra_proposta_pregao/(?P<pregao_id>\d+)/$', views.cadastra_proposta_pregao, name='cadastra_proposta_pregao'),
    url(r'^propostas_item/(?P<item_id>\d+)/$', views.propostas_item, name='propostas_item'),
    url(r'^propostas_item_credenciamento/(?P<item_id>\d+)/$', views.propostas_item_credenciamento, name='propostas_item_credenciamento'),

    url(r'^gerar_resultado_licitacao_toda/(?P<pregao_id>\d+)/$', views.gerar_resultado_licitacao_toda, name='gerar_resultado_licitacao_toda'),

    url(r'^lances_item/(?P<item_id>\d+)/$', views.lances_item, name='lances_item'),
    url(r'^rodada_pregao/(?P<item_id>\d+)/$', views.rodada_pregao, name='rodada_pregao'),
    url(r'^declinar_lance/(?P<rodada_id>\d+)/(?P<item_id>\d+)/(?P<participante_id>\d+)/$', views.declinar_lance, name='declinar_lance'),
    url(r'^baixar_editais/$', views.baixar_editais, name='baixar_editais'),
    url(r'^ver_solicitacoes/$', views.ver_solicitacoes, name='ver_solicitacoes'),
    url(r'^rejeitar_solicitacao/(?P<solicitacao_id>\d+)/$', views.rejeitar_solicitacao, name='rejeitar_solicitacao'),
    url(r'^cadastrar_pregao/(?P<solicitacao_id>\d+)/$', views.cadastrar_pregao, name='cadastrar_pregao'),
    url(r'^enviar_para_licitacao/(?P<solicitacao_id>\d+)/$', views.enviar_para_licitacao, name='enviar_para_licitacao'),
    url(r'^movimentar_solicitacao/(?P<solicitacao_id>\d+)/(?P<tipo>\d+)/$', views.movimentar_solicitacao, name='movimentar_solicitacao'),
    url(r'^registrar_preco_item/(?P<item_id>\d+)/$', views.registrar_preco_item, name='registrar_preco_item'),
    url(r'^cadastra_participante_pregao/(?P<pregao_id>\d+)/$', views.cadastra_participante_pregao, name='cadastra_participante_pregao'),
    url(r'^ver_fornecedores/$', views.ver_fornecedores, name='ver_fornecedores'),
    url(r'^ver_fornecedores/(?P<fornecedor_id>\d+)/$', views.ver_fornecedores, name='ver_fornecedores'),
    url(r'^ver_pregoes/$', views.ver_pregoes, name='ver_pregoes'),
    url(r'^cadastrar_solicitacao/$', views.cadastrar_solicitacao, name='cadastrar_solicitacao'),
    url(r'^pesquisa_mercadologica/(?P<solicitacao_id>\d+)/$', views.pesquisa_mercadologica, name='pesquisa_mercadologica'),
    url(r'^preencher_pesquisa_mercadologica/(?P<solicitacao_id>\d+)/$', views.preencher_pesquisa_mercadologica, name='preencher_pesquisa_mercadologica'),
    url(r'^preencher_itens_pesquisa_mercadologica/(?P<solicitacao_id>\d+)/(?P<origem>\d+)/$', views.preencher_itens_pesquisa_mercadologica, name='preencher_itens_pesquisa_mercadologica'),
    url(r'^upload_pesquisa_mercadologica/(?P<pesquisa_id>\d+)/$', views.upload_pesquisa_mercadologica, name='upload_pesquisa_mercadologica'),
    url(r'^imprimir_pesquisa/(?P<pesquisa_id>\d+)/$', views.imprimir_pesquisa, name='imprimir_pesquisa'),
    url(r'^ver_pesquisa_mercadologica/(?P<item_id>\d+)/$', views.ver_pesquisa_mercadologica, name='ver_pesquisa_mercadologica'),
    url(r'^resultado_classificacao/(?P<item_id>\d+)/$', views.resultado_classificacao, name='resultado_classificacao'),
    url(r'^desclassificar_do_pregao/(?P<participante_id>\d+)/$', views.desclassificar_do_pregao, name='desclassificar_do_pregao'),
    url(r'^planilha_propostas/(?P<solicitacao_id>\d+)/$', views.planilha_propostas, name='planilha_propostas'),
    url(r'^remover_participante/(?P<proposta_id>\d+)/(?P<situacao>\d+)/$', views.remover_participante, name='remover_participante'),
    url(r'^adicionar_por_discricionaridade/(?P<proposta_id>\d+)/$', views.adicionar_por_discricionaridade, name='adicionar_por_discricionaridade'),
    url(r'^gerar_resultado/(?P<item_id>\d+)/$', views.gerar_resultado, name='gerar_resultado'),
    url(r'^resultado_alterar/(?P<resultado_id>\d+)/(?P<situacao>\d+)/$', views.resultado_alterar, name='resultado_alterar'),
    url(r'^resultado_ajustar_preco/(?P<resultado_id>\d+)/$', views.resultado_ajustar_preco, name='resultado_ajustar_preco'),
    url(r'^desempatar_item/(?P<item_id>\d+)/$', views.desempatar_item, name='desempatar_item'),
    url(r'^definir_colocacao/(?P<resultado_id>\d+)/$', views.definir_colocacao, name='definir_colocacao'),
    url(r'^cadastrar_anexo_pregao/(?P<pregao_id>\d+)/$', views.cadastrar_anexo_pregao, name='cadastrar_anexo_pregao'),
    url(r'^baixar_arquivo/(?P<arquivo_id>\d+)/$', views.baixar_arquivo, name='baixar_arquivo'),
    url(r'^alterar_valor_lance/(?P<lance_id>\d+)/$', views.alterar_valor_lance, name='alterar_valor_lance'),
    url(r'^avancar_proximo_item/(?P<item_id>\d+)/$', views.avancar_proximo_item, name='avancar_proximo_item'),
    url(r'^cancelar_rodada/(?P<item_id>\d+)/$', views.cancelar_rodada, name='cancelar_rodada'),
    url(r'^editar_proposta/(?P<proposta_id>\d+)/$', views.editar_proposta, name='editar_proposta'),
    url(r'^encerrar_pregao/(?P<pregao_id>\d+)/(?P<motivo>\d+)/$', views.encerrar_pregao, name='encerrar_pregao'),
    url(r'^encerrar_itempregao/(?P<item_id>\d+)/(?P<motivo>\d+)/(?P<origem>\d+)/$', views.encerrar_itempregao, name='encerrar_itempregao'),
    url(r'^suspender_pregao/(?P<pregao_id>\d+)/$', views.suspender_pregao, name='suspender_pregao'),
    url(r'^prazo_pesquisa_mercadologica/(?P<solicitacao_id>\d+)/$', views.prazo_pesquisa_mercadologica, name='prazo_pesquisa_mercadologica'),
    url(r'^resultado_alterar_todos/(?P<pregao_id>\d+)/(?P<participante_id>\d+)/(?P<situacao>\d+)/$', views.resultado_alterar_todos, name='resultado_alterar_todos'),
    url(r'^relatorio_economia/(?P<pregao_id>\d+)/$', views.relatorio_economia, name='relatorio_economia'),
    url(r'^revogar_pregao/(?P<pregao_id>\d+)/$', views.revogar_pregao, name='revogar_pregao'),
    url(r'^cadastra_visitante_pregao/(?P<pregao_id>\d+)/$', views.cadastra_visitante_pregao, name='cadastra_visitante_pregao'),
    url(r'^relatorio_lista_visitantes/(?P<pregao_id>\d+)/$', views.relatorio_lista_visitantes, name='relatorio_lista_visitantes'),
    url(r'^gerenciar_visitantes/(?P<pregao_id>\d+)/$', views.gerenciar_visitantes, name='gerenciar_visitantes'),
    url(r'^editar_visitante/(?P<visitante_id>\d+)/$', views.editar_visitante, name='editar_visitante'),
    url(r'^excluir_visitante/(?P<visitante_id>\d+)/$', views.excluir_visitante, name='excluir_visitante'),
    url(r'^gerar_resultado_credenciamento/(?P<pregao_id>\d+)/$', views.gerar_resultado_credenciamento, name='gerar_resultado_credenciamento'),
    url(r'^salvar_sorteio_item_pregao/(?P<item_id>\d+)/$', views.salvar_sorteio_item_pregao, name='salvar_sorteio_item_pregao'),
    url(r'^mudar_credenciamento_fornecedor/(?P<credenciamento_id>\d+)/(?P<fornecedor_id>\d+)/(?P<opcao>\d+)/$', views.mudar_credenciamento_fornecedor, name='mudar_credenciamento_fornecedor'),

    url(r'^imprimir_aditivo/(?P<aditivo_id>\d+)/$', views.imprimir_aditivo, name='imprimir_aditivo'),
    url(r'^transferir_quantidade_item_arp/(?P<itemarp_id>\d+)/$', views.transferir_quantidade_item_arp, name='transferir_quantidade_item_arp'),
    url(r'^busca_saldo_atual/$', views.busca_saldo_atual, name='busca_saldo_atual'),

    url(r'^cadastrar_credenciamento/(?P<solicitacao_id>\d+)/$', views.cadastrar_credenciamento, name='cadastrar_credenciamento'),
    url(r'^imprimir_fornecedor/(?P<fornecedor_id>\d+)/$', views.imprimir_fornecedor, name='imprimir_fornecedor'),
    url(r'^visualizar_credenciamento/(?P<credenciamento_id>\d+)/$', views.visualizar_credenciamento, name='visualizar_credenciamento'),


    url(r'^modelo_memorando/(?P<solicitacao_id>\d+)/$', views.modelo_memorando, name='modelo_memorando'),
    url(r'^receber_solicitacao/(?P<solicitacao_id>\d+)/$', views.receber_solicitacao, name='receber_solicitacao'),
    url(r'^ver_movimentacao/(?P<solicitacao_id>\d+)/$', views.ver_movimentacao, name='ver_movimentacao'),
    url(r'^cadastrar_minuta/(?P<solicitacao_id>\d+)/$', views.cadastrar_minuta, name='cadastrar_minuta'),
    url(r'^avalia_minuta/(?P<solicitacao_id>\d+)/(?P<tipo>\d+)/$', views.avalia_minuta, name='avalia_minuta'),
    url(r'^retomar_lances/(?P<item_id>\d+)/$', views.retomar_lances, name='retomar_lances'),
    url(r'^informar_quantidades/(?P<solicitacao_id>\d+)/$', views.informar_quantidades, name='informar_quantidades'),
    url(r'^ver_pedidos_secretaria/(?P<item_id>\d+)/$', views.ver_pedidos_secretaria, name='ver_pedidos_secretaria'),
    url(r'^importar_itens/(?P<solicitacao_id>\d+)/$', views.importar_itens, name='importar_itens'),
    url(r'^planilha_pesquisa_mercadologica/(?P<solicitacao_id>\d+)/$', views.planilha_pesquisa_mercadologica, name='planilha_pesquisa_mercadologica'),
    url(r'^upload_itens_pesquisa_mercadologica/(?P<pesquisa_id>\d+)/$', views.upload_itens_pesquisa_mercadologica, name='upload_itens_pesquisa_mercadologica'),
    url(r'^relatorio_resultado_final/(?P<pregao_id>\d+)/$', views.relatorio_resultado_final, name='relatorio_resultado_final'),
    url(r'^relatorio_resultado_final_por_vencedor/(?P<pregao_id>\d+)/$', views.relatorio_resultado_final_por_vencedor, name='relatorio_resultado_final_por_vencedor'),
    url(r'^relatorio_lista_participantes/(?P<pregao_id>\d+)/$', views.relatorio_lista_participantes, name='relatorio_lista_participantes'),
    url(r'^relatorio_classificacao_por_item/(?P<pregao_id>\d+)/$', views.relatorio_classificacao_por_item, name='relatorio_classificacao_por_item'),
    url(r'^relatorio_ocorrencias/(?P<pregao_id>\d+)/$', views.relatorio_ocorrencias, name='relatorio_ocorrencias'),
    url(r'^relatorio_lances_item/(?P<pregao_id>\d+)/$', views.relatorio_lances_item, name='relatorio_lances_item'),
    url(r'^relatorio_ata_registro_preco/(?P<pregao_id>\d+)/$', views.relatorio_ata_registro_preco, name='relatorio_ata_registro_preco'),
    url(r'^pedido_outro_interessado/(?P<pedido_id>\d+)/(?P<opcao>\d+)/$', views.pedido_outro_interessado, name='pedido_outro_interessado'),
    url(r'^abrir_processo_para_solicitacao/(?P<solicitacao_id>\d+)/$', views.abrir_processo_para_solicitacao, name='abrir_processo_para_solicitacao'),
    url(r'^ver_processo/(?P<processo_id>\d+)/$', views.ver_processo, name='ver_processo'),
    url(r'^imprimir_capa_processo/(?P<processo_id>\d+)/$', views.imprimir_capa_processo, name='imprimir_capa_processo'),
    url(r'^criar_lote/(?P<pregao_id>\d+)/$', views.criar_lote, name='criar_lote'),
    url(r'^extrato_inicial/(?P<pregao_id>\d+)/$', views.extrato_inicial, name='extrato_inicial'),
    url(r'^relatorio_propostas_pregao/(?P<pregao_id>\d+)/$', views.relatorio_propostas_pregao, name='relatorio_propostas_pregao'),
    url(r'^termo_adjudicacao/(?P<pregao_id>\d+)/$', views.termo_adjudicacao, name='termo_adjudicacao'),
    url(r'^editar_meu_perfil/(?P<pessoa_id>\d+)/$', views.editar_meu_perfil, name='editar_meu_perfil'),
    url(r'^editar_pedido/(?P<pedido_id>\d+)/$', views.editar_pedido, name='editar_pedido'),
    url(r'^aprovar_todos_pedidos/(?P<item_id>\d+)/$', views.aprovar_todos_pedidos, name='aprovar_todos_pedidos'),
    url(r'^gestao_pedidos/(?P<tipo_id>\d+)/$', views.gestao_pedidos, name='gestao_pedidos'),
    url(r'^gestao_contratos_tipo/$', views.gestao_contratos_tipo, name='gestao_contratos_tipo'),
    url(r'^gestao_contratos/(?P<tipo_id>\d+)/$', views.gestao_contratos, name='gestao_contratos'),
    url(r'^ver_ordem_compra_dispensa/(?P<solicitacao_id>\d+)/$', views.ver_ordem_compra_dispensa, name='ver_ordem_compra_dispensa'),
    url(r'^excluir_solicitacao_pedido/(?P<solicitacao_id>\d+)/$', views.excluir_solicitacao_pedido, name='excluir_solicitacao_pedido'),



    url(r'^avaliar_pedidos/(?P<solicitacao_id>\d+)/$', views.avaliar_pedidos, name='avaliar_pedidos'),
    url(r'^aprovar_todos_pedidos_secretaria/(?P<solicitacao_id>\d+)/(?P<secretaria_id>\d+)/$', views.aprovar_todos_pedidos_secretaria, name='aprovar_todos_pedidos_secretaria'),


    url(r'^apagar_anexo_pregao/(?P<item_id>\d+)/$', views.apagar_anexo_pregao, name='apagar_anexo_pregao'),
    url(r'^gerar_pedido_fornecedores/(?P<solicitacao_id>\d+)/$', views.gerar_pedido_fornecedores, name='gerar_pedido_fornecedores'),
    url(r'^apagar_lote/(?P<item_id>\d+)/(?P<pregao_id>\d+)/$', views.apagar_lote, name='apagar_lote'),
    url(r'^informar_valor_final_item_lote/(?P<item_id>\d+)/(?P<pregao_id>\d+)/$', views.informar_valor_final_item_lote, name='informar_valor_final_item_lote'),
    url(r'^gerar_ordem_compra/(?P<solicitacao_id>\d+)/$', views.gerar_ordem_compra, name='gerar_ordem_compra'),
    url(r'^ver_ordem_compra/(?P<solicitacao_id>\d+)/$', views.ver_ordem_compra, name='ver_ordem_compra'),
    url(r'^registrar_adjudicacao/(?P<pregao_id>\d+)/$', views.registrar_adjudicacao, name='registrar_adjudicacao'),
    url(r'^registrar_homologacao/(?P<pregao_id>\d+)/$', views.registrar_homologacao, name='registrar_homologacao'),
    url(r'^termo_homologacao/(?P<pregao_id>\d+)/$', views.termo_homologacao, name='termo_homologacao'),
    url(r'^visualizar_contrato/(?P<solicitacao_id>\d+)/$', views.visualizar_contrato, name='visualizar_contrato'),
    url(r'^liberar_solicitacao_contrato/(?P<solicitacao_id>\d+)/(?P<origem>\d+)/$', views.liberar_solicitacao_contrato, name='liberar_solicitacao_contrato'),
    url(r'^liberar_solicitacao_credenciamento/(?P<credenciamento_id>\d+)/(?P<origem>\d+)/$', views.liberar_solicitacao_credenciamento, name='liberar_solicitacao_credenciamento'),
    url(r'^definir_vigencia_contrato/(?P<contrato_id>\d+)/$', views.definir_vigencia_contrato, name='definir_vigencia_contrato'),
    url(r'^aditivar_contrato/(?P<contrato_id>\d+)/$', views.aditivar_contrato, name='aditivar_contrato'),
    url(r'^memorando/(?P<solicitacao_id>\d+)/$', views.memorando, name='memorando'),
    url(r'^termo_referencia/(?P<solicitacao_id>\d+)/$', views.termo_referencia, name='termo_referencia'),
    url(r'^lista_materiais/(?P<solicitacao_id>\d+)/$', views.lista_materiais, name='lista_materiais'),
    url(r'^apagar_documento/(?P<documento_id>\d+)/$', views.apagar_documento, name='apagar_documento'),
    url(r'^cadastrar_fornecedor/(?P<opcao>\d+)/$', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    url(r'^editar_fornecedor/(?P<fornecedor_id>\d+)/$', views.editar_fornecedor, name='editar_fornecedor'),
    url(r'^remover_participante_pregao/(?P<participante_id>\d+)/$', views.remover_participante_pregao, name='remover_participante_pregao'),


    url(r'^editar_solicitacao/(?P<solicitacao_id>\d+)/$', views.editar_solicitacao, name='editar_solicitacao'),
    url(r'^cadastrar_material/(?P<solicitacao_id>\d+)/$', views.cadastrar_material, name='cadastrar_material'),
    url(r'^lista_documentos/(?P<solicitacao_id>\d+)/$', views.lista_documentos, name='lista_documentos'),
    url(r'^cadastrar_documento/(?P<solicitacao_id>\d+)/$', views.cadastrar_documento, name='cadastrar_documento'),
    url(r'^editar_pregao/(?P<pregao_id>\d+)/$', views.editar_pregao, name='editar_pregao'),
    url(r'^upload_termo_homologacao/(?P<pregao_id>\d+)/$', views.upload_termo_homologacao, name='upload_termo_homologacao'),
    url(r'^gerar_resultado_licitacao/(?P<pregao_id>\d+)/$', views.gerar_resultado_licitacao, name='gerar_resultado_licitacao'),
    url(r'^cadastrar_anexo_contrato/(?P<contrato_id>\d+)/$', views.cadastrar_anexo_contrato, name='cadastrar_anexo_contrato'),
    url(r'^editar_anexo_contrato/(?P<item_id>\d+)/$', views.editar_anexo_contrato, name='editar_anexo_contrato'),
    url(r'^liberar_licitacao_homologacao/(?P<pregao_id>\d+)/$', views.liberar_licitacao_homologacao, name='liberar_licitacao_homologacao'),
    url(r'^relatorio_dados_licitacao/(?P<pregao_id>\d+)/$', views.relatorio_dados_licitacao, name='relatorio_dados_licitacao'),
    url(r'^relatorio_itens_desertos/(?P<pregao_id>\d+)/$', views.relatorio_itens_desertos, name='relatorio_itens_desertos'),



    url(r'^apagar_anexo_contrato/(?P<item_id>\d+)/$', views.apagar_anexo_contrato, name='apagar_anexo_contrato'),
    url(r'^documentos_atas/(?P<ata_id>\d+)/$', views.documentos_atas, name='documentos_atas'),
    url(r'^documentos_contratos/(?P<contrato_id>\d+)/$', views.documentos_contratos, name='documentos_contratos'),
    url(r'^documentos_credenciamentos/(?P<credenciamento_id>\d+)/$', views.documentos_credenciamentos, name='documentos_credenciamentos'),

    url(r'^editar_cnaes_secundario/(?P<item_id>\d+)/$', views.editar_cnaes_secundario, name='editar_cnaes_secundario'),
    url(r'^excluir_cnaes_secundario/(?P<item_id>\d+)/$', views.excluir_cnaes_secundario, name='excluir_cnaes_secundario'),

    url(r'^editar_socio/(?P<item_id>\d+)/$', views.editar_socio, name='editar_socio'),
    url(r'^excluir_socio/(?P<item_id>\d+)/$', views.excluir_socio, name='excluir_socio'),
    url(r'^aditivar_contrato/(?P<contrato_id>\d+)/$', views.aditivar_contrato, name='aditivar_contrato'),



    url(r'^rejeitar_pesquisa/(?P<item_pesquisa_id>\d+)/$', views.rejeitar_pesquisa, name='rejeitar_pesquisa'),
    url(r'^excluir_item_pesquisa/(?P<item_pesquisa_id>\d+)/$', views.excluir_item_pesquisa, name='excluir_item_pesquisa'),
    url(r'^ver_pesquisas/(?P<solicitacao_id>\d+)/$', views.ver_pesquisas, name='ver_pesquisas'),
    url(r'^excluir_pesquisa/(?P<pesquisa_id>\d+)/$', views.excluir_pesquisa, name='excluir_pesquisa'),


    url(r'^cadastrar_contrato/(?P<solicitacao_id>\d+)/$', views.cadastrar_contrato, name='cadastrar_contrato'),
    url(r'^relatorio_lista_download_licitacao/(?P<pregao_id>\d+)/$', views.relatorio_lista_download_licitacao, name='relatorio_lista_download_licitacao'),
    url(r'^registrar_ocorrencia_pregao/(?P<pregao_id>\d+)/$', views.registrar_ocorrencia_pregao, name='registrar_ocorrencia_pregao'),
    url(r'^ata_sessao/(?P<pregao_id>\d+)/$', views.ata_sessao, name='ata_sessao'),
    url(r'^ata_sessao_credenciamento/(?P<pregao_id>\d+)/$', views.ata_sessao_credenciamento, name='ata_sessao_credenciamento'),

    url(r'^adicionar_membro_comissao/(?P<comissao_id>\d+)/$', views.adicionar_membro_comissao, name='adicionar_membro_comissao'),
    url(r'^remover_membro_comissao/(?P<comissao_id>\d+)/$', views.remover_membro_comissao, name='remover_membro_comissao'),
    url(r'^editar_membro_comissao/(?P<membro_id>\d+)/$', views.editar_membro_comissao, name='editar_membro_comissao'),
    url(r'^editar_item/(?P<item_id>\d+)/$', views.editar_item, name='editar_item'),

    url(r'^solicitar_pedidos_novamente/(?P<solicitacao_id>\d+)/(?P<secretaria_id>\d+)/$', views.solicitar_pedidos_novamente, name='solicitar_pedidos_novamente'),
    url(r'^editar_item_pedido/(?P<pedido_id>\d+)/(?P<tipo>\d+)/$', views.editar_item_pedido, name='editar_item_pedido'),
    url(r'^apagar_item_pedido/(?P<pedido_id>\d+)/(?P<tipo>\d+)/$', views.apagar_item_pedido, name='apagar_item_pedido'),

    url(r'^ver_crc/(?P<fornecedor_id>\d+)/$', views.ver_crc, name='ver_crc'),
    url(r'^cadastrar_crc/(?P<fornecedor_id>\d+)/$', views.cadastrar_crc, name='cadastrar_crc'),
    url(r'^imprimir_crc/(?P<fornecedor_id>\d+)/$', views.imprimir_crc, name='imprimir_crc'),
    url(r'^cadastrar_cnaes_secundario/(?P<crc_id>\d+)/$', views.cadastrar_cnaes_secundario, name='cadastrar_cnaes_secundario'),
    url(r'^cadastrar_socio/(?P<crc_id>\d+)/$', views.cadastrar_socio, name='cadastrar_socio'),
    url(r'^renovar_crc/(?P<fornecedor_id>\d+)/$', views.renovar_crc, name='renovar_crc'),


    url(r'^excluir_ordem_compra_dispensa/(?P<solicitacao_id>\d+)/$', views.excluir_ordem_compra_dispensa, name='excluir_ordem_compra_dispensa'),



    url(r'^novo_pedido_compra_contrato/(?P<contrato_id>\d+)/$', views.novo_pedido_compra_contrato, name='novo_pedido_compra_contrato'),
    url(r'^novo_pedido_compra_contrato/(?P<contrato_id>\d+)/(?P<lote_id>\d+)/$', views.novo_pedido_compra_contrato, name='novo_pedido_compra_contrato'),
    url(r'^novo_pedido_compra_arp/(?P<ata_id>\d+)/$', views.novo_pedido_compra_arp, name='novo_pedido_compra_arp'),
    url(r'^novo_pedido_compra_credenciamento/(?P<credenciamento_id>\d+)/$', views.novo_pedido_compra_credenciamento, name='novo_pedido_compra_credenciamento'),



    url(r'^informar_quantidades_do_pedido_contrato/(?P<contrato_id>\d+)/(?P<solicitacao_id>\d+)/$', views.informar_quantidades_do_pedido_contrato, name='informar_quantidades_do_pedido_contrato'),
    url(r'^informar_quantidades_do_pedido_contrato/(?P<contrato_id>\d+)/(?P<solicitacao_id>\d+)/(?P<lote_id>\d+)/$', views.informar_quantidades_do_pedido_contrato, name='informar_quantidades_do_pedido_contrato'),


    url(r'^informar_quantidades_do_pedido_arp/(?P<ata_id>\d+)/(?P<solicitacao_id>\d+)/$', views.informar_quantidades_do_pedido_arp, name='informar_quantidades_do_pedido_arp'),
    url(r'^informar_quantidades_do_pedido_credenciamento/(?P<credenciamento_id>\d+)/(?P<solicitacao_id>\d+)/$', views.informar_quantidades_do_pedido_credenciamento, name='informar_quantidades_do_pedido_credenciamento'),


    url(r'^cadastrar_ata_registro_preco/(?P<solicitacao_id>\d+)/$', views.cadastrar_ata_registro_preco, name='cadastrar_ata_registro_preco'),


    url(r'^visualizar_ata_registro_preco/(?P<ata_id>\d+)/$', views.visualizar_ata_registro_preco, name='visualizar_ata_registro_preco'),


    url(r'^liberar_solicitacao_ata/(?P<ata_id>\d+)/(?P<origem>\d+)/$', views.liberar_solicitacao_ata, name='liberar_solicitacao_ata'),


    url(r'^baixar_atas/$', views.baixar_atas, name='baixar_atas'),
    url(r'^baixar_contratos/$', views.baixar_contratos, name='baixar_contratos'),

    url(r'^cadastrar_anexo_arp/(?P<ata_id>\d+)/$', views.cadastrar_anexo_arp, name='cadastrar_anexo_arp'),
    url(r'^editar_anexo_arp/(?P<item_id>\d+)/$', views.editar_anexo_arp, name='editar_anexo_arp'),

    url(r'^cadastrar_material_arp/(?P<ata_id>\d+)/$', views.cadastrar_material_arp, name='cadastrar_material_arp'),
    url(r'^liberar_pedidos_solicitacao/(?P<solicitacao_id>\d+)/$', views.liberar_pedidos_solicitacao, name='liberar_pedidos_solicitacao'),
    url(r'^cadastrar_termo_inexigibilidade/(?P<solicitacao_id>\d+)/$', views.cadastrar_termo_inexigibilidade, name='cadastrar_termo_inexigibilidade'),
    url(r'^cadastrar_termo_referencia/(?P<solicitacao_id>\d+)/$', views.cadastrar_termo_referencia, name='cadastrar_termo_referencia'),
    url(r'^enviar_convites/(?P<solicitacao_id>\d+)/$', views.enviar_convites, name='enviar_convites'),

    url(r'^relatorio_propostas/(?P<solicitacao_id>\d+)/$', views.relatorio_propostas, name='relatorio_propostas'),
    url(r'^rescindir_contrato/(?P<contrato_id>\d+)/$', views.rescindir_contrato, name='rescindir_contrato'),
    url(r'^contratar_remanescentes/(?P<contrato_id>\d+)/$', views.contratar_remanescentes, name='contratar_remanescentes'),





    url(r'^apagar_anexo_arp/(?P<item_id>\d+)/$', views.apagar_anexo_arp, name='apagar_anexo_arp'),
    url(r'^aderir_arp/$', views.aderir_arp, name='aderir_arp'),
    url(r'^adicionar_item_adesao_arp/(?P<ata_id>\d+)/$', views.adicionar_item_adesao_arp, name='adicionar_item_adesao_arp'),
    url(r'^criar_contrato_adesao_ata/(?P<ata_id>\d+)/$', views.criar_contrato_adesao_ata, name='criar_contrato_adesao_ata'),
    url(r'^carregar_planilha_itens_adesao_arp/(?P<ata_id>\d+)/$', views.carregar_planilha_itens_adesao_arp, name='carregar_planilha_itens_adesao_arp'),

    url(r'^cadastrar_anexo_credenciamento/(?P<credenciamento_id>\d+)/$', views.cadastrar_anexo_credenciamento, name='cadastrar_anexo_credenciamento'),
    url(r'^cadastrar_empresa_credenciamento/(?P<credenciamento_id>\d+)/$', views.cadastrar_empresa_credenciamento, name='cadastrar_empresa_credenciamento'),
    url(r'^informar_quantidades_do_pedido_adesao_arp/(?P<ata_id>\d+)/(?P<solicitacao_id>\d+)/$', views.informar_quantidades_do_pedido_adesao_arp, name='informar_quantidades_do_pedido_adesao_arp'),

    url(r'^editar_anexo_credenciamento/(?P<item_id>\d+)/$', views.editar_anexo_credenciamento, name='editar_anexo_credenciamento'),
    url(r'^apagar_anexo_credenciamento/(?P<item_id>\d+)/$', views.apagar_anexo_credenciamento, name='apagar_anexo_credenciamento'),
    url(r'^anexo_38/(?P<pregao_id>\d+)/$', views.anexo_38, name='anexo_38'),



    url(r'^lista_materiais_por_secretaria/(?P<solicitacao_id>\d+)/(?P<secretaria_id>\d+)/$', views.lista_materiais_por_secretaria, name='lista_materiais_por_secretaria'),
    url(r'^apagar_item/(?P<item_id>\d+)/$', views.apagar_item, name='apagar_item'),
    url(r'^editar_valor_final/(?P<item_id>\d+)/(?P<pregao_id>\d+)/$', views.editar_valor_final, name='editar_valor_final'),
    url(r'^gerar_resultado_item_pregao/(?P<item_id>\d+)/$', views.gerar_resultado_item_pregao, name='gerar_resultado_item_pregao'),

    url(r'^gerenciar_grupos/$', views.gerenciar_grupos, name='gerenciar_grupos'),
    url(r'^ver_variaveis_configuracao/$', views.ver_variaveis_configuracao, name='ver_variaveis_configuracao'),
    url(r'^cadastrar_variaveis_configuracao/$', views.cadastrar_variaveis_configuracao, name='cadastrar_variaveis_configuracao'),
    url(r'^notificacoes/$', views.notificacoes, name='notificacoes'),
    url(r'^editar_item_arp/(?P<item_id>\d+)/$', views.editar_item_arp, name='editar_item_arp'),
    url(r'^apagar_item_arp/(?P<item_id>\d+)/$', views.apagar_item_arp, name='apagar_item_arp'),
    url(r'^cadastrar_certidao_crc/(?P<crc_id>\d+)/$', views.cadastrar_certidao_crc, name='cadastrar_certidao_crc'),

    url(r'^sortear_inicio_lances/(?P<item_id>\d+)/$', views.sortear_inicio_lances, name='sortear_inicio_lances'),



    url(r'^localizar_processo/$', views.localizar_processo, name='localizar_processo'),
    url(r'^ver_relatorios_gerenciais_licitacao/$', views.ver_relatorios_gerenciais_licitacao, name='ver_relatorios_gerenciais_licitacao'),
    url(r'^ver_relatorios_gerenciais_contratos/$', views.ver_relatorios_gerenciais_contratos, name='ver_relatorios_gerenciais_contratos'),
    url(r'^ver_relatorios_gerenciais_atas/$', views.ver_relatorios_gerenciais_atas, name='ver_relatorios_gerenciais_atas'),
    url(r'^ver_relatorios_gerenciais_credenciamentos/$', views.ver_relatorios_gerenciais_credenciamentos, name='ver_relatorios_gerenciais_credenciamentos'),
    url(r'^ver_relatorios_gerenciais_compras/$', views.ver_relatorios_gerenciais_compras, name='ver_relatorios_gerenciais_compras'),


    url(r'^relatorio_info_contrato/(?P<contrato_id>\d+)/$', views.relatorio_info_contrato, name='relatorio_info_contrato'),
    url(r'^relatorio_qtd_disponivel_contrato/(?P<contrato_id>\d+)/$', views.relatorio_qtd_disponivel_contrato, name='relatorio_qtd_disponivel_contrato'),
    url(r'^relatorio_qtd_consumida_contrato/(?P<contrato_id>\d+)/$', views.relatorio_qtd_consumida_contrato, name='relatorio_qtd_consumida_contrato'),

    url(r'^relatorio_info_arp/(?P<ata_id>\d+)/$', views.relatorio_info_arp, name='relatorio_info_arp'),
    url(r'^relatorio_qtd_disponivel_ata/(?P<ata_id>\d+)/(?P<fornecedor_id>\d+)/$', views.relatorio_qtd_disponivel_ata, name='relatorio_qtd_disponivel_ata'),
    url(r'^relatorio_qtd_consumida_ata/(?P<ata_id>\d+)/(?P<fornecedor_id>\d+)/$', views.relatorio_qtd_consumida_ata, name='relatorio_qtd_consumida_ata'),
    url(r'^relatorio_saldo_ata_secretaria/(?P<ata_id>\d+)/(?P<secretaria_id>\d+)/$', views.relatorio_saldo_ata_secretaria, name='relatorio_saldo_ata_secretaria'),


    url(r'^relatorio_info_credenciamento/(?P<credenciamento_id>\d+)/$', views.relatorio_info_credenciamento, name='relatorio_info_credenciamento'),
    url(r'^relatorio_qtd_disponivel_credenciamento/(?P<credenciamento_id>\d+)/$', views.relatorio_qtd_disponivel_credenciamento, name='relatorio_qtd_disponivel_credenciamento'),
    url(r'^relatorio_qtd_consumida_credenciamento/(?P<credenciamento_id>\d+)/$', views.relatorio_qtd_consumida_credenciamento, name='relatorio_qtd_consumida_credenciamento'),

    url(r'^gerenciar_grupo_usuario/(?P<usuario_id>\d+)/(?P<grupo_id>\d+)/(?P<acao>\d+)/$', views.gerenciar_grupo_usuario, name='gerenciar_grupo_usuario'),
    url(r'^informar_valor_final_itens_lote/(?P<lote_id>\d+)/(?P<pregao_id>\d+)/$', views.informar_valor_final_itens_lote, name='informar_valor_final_itens_lote'),
    url(r'^informar_desconto_final_itens_lote/(?P<lote_id>\d+)/(?P<pregao_id>\d+)/$', views.informar_desconto_final_itens_lote, name='informar_desconto_final_itens_lote'),

    url(r'^secretaria-autocomplete/$', SecretariaAutocomplete.as_view(), name='secretaria-autocomplete'),
    url(r'^participantepregao-autocomplete/$', ParticipantePregaoAutocomplete.as_view(), name='participantepregao-autocomplete'),
    url(r'^pessoafisica-autocomplete/$', PessoaFisicaAutocomplete.as_view(), name='pessoafisica-autocomplete'),
    url(r'^materialconsumo-autocomplete/$', MaterialConsumoAutocomplete.as_view(), name='materialconsumo-autocomplete'),
    url(r'^fornecedor-autocomplete/$', FornecedorAutocomplete.as_view(), name='fornecedor-autocomplete'),


    url(r'^ativar_item_pregao/(?P<item_id>\d+)/$', views.ativar_item_pregao, name='ativar_item_pregao'),
    url(r'^editar_processo/(?P<processo_id>\d+)/$', views.editar_processo, name='editar_processo'),
    url(r'^editar_certidao/(?P<certidao_id>\d+)/$', views.editar_certidao, name='editar_certidao'),
    url(r'^trocar_senha/(?P<username>\w+)/(?P<token>\w+)/$', views.trocar_senha, name='trocar_senha'),
    url(r'^solicitar_mudanca_senha/$', views.solicitar_mudanca_senha, name='solicitar_mudanca_senha'),
    url(r'^ver_calendario/$', views.ver_calendario, name='ver_calendario'),
    url(r'^ver_lista_feriados/$', views.ver_lista_feriados, name='ver_lista_feriados'),
    url(r'^cadastrar_unidade/(?P<solicitacao_id>\d+)/$', views.cadastrar_unidade, name='cadastrar_unidade'),

    url(r'^gerar_xml_comprasnet/(?P<pregao_id>\d+)/$', views.gerar_xml_comprasnet, name='gerar_xml_comprasnet'),
    url(r'^comprasnet/(?P<pregao_id>\d+)/$', views.comprasnet, name='comprasnet'),

    url(r'^pregoes/$', PregaoView.as_view({'get': 'list'}), name="pregoes"),
    url(r'^pregoes/(?P<pk>\d+)/$', PregaoView.as_view({'get': 'retrieve'}), name="pregoes_get"),
    url(r'^atas/$', ARPView.as_view({'get': 'list'}), name="atas"),
    url(r'^atas/(?P<pk>\d+)/$', ARPView.as_view({'get': 'retrieve'}), name="atas_get"),
    url(r'^anexo_10/$', views.anexo_10, name='anexo_10'),
    url(r'^anexo_11/$', views.anexo_11, name='anexo_11'),
    url(r'^relatorios_tce/$', views.relatorios_tce, name='relatorios_tce'),
    url(r'^imprime_convites_enviados/(?P<solicitacao_id>\d+)/$', views.imprime_convites_enviados, name='imprime_convites_enviados'),
    url(r'^pedidos_arp_secretarias/(?P<ata_id>\d+)/$', views.pedidos_arp_secretarias, name='pedidos_arp_secretarias'),

    url(r'^inativar_item_arp/(?P<item_id>\d+)/$', views.inativar_item_arp, name='inativar_item_arp'),
    url(r'^inativar_item_contrato/(?P<item_id>\d+)/$', views.inativar_item_contrato, name='inativar_item_contrato'),
    url(r'^desliga_users/$', views.desliga_users, name='desliga_users'),
    url(r'^liga_users/$', views.liga_users, name='liga_users'),
    url(r'^contratos_atas_fornecedor/(?P<fornecedor_id>\d+)/$', views.contratos_atas_fornecedor, name='contratos_atas_fornecedor'),

]




