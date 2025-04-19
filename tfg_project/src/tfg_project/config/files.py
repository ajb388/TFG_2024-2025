from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

class files():

    json_humanidades = JSONKnowledgeSource(
        file_paths='/cafeterias/cafeteria_humanidades.json',
        knowledge_source_name='cafeteria_humanidades',
        verbose=True,
    )

    json_cae = JSONKnowledgeSource(
        file_paths='/cafeterias/cafeteria_cae.json',
        knowledge_source_name='cafeteria_cae',
        verbose=True,
    )

    json_central = JSONKnowledgeSource(
        file_paths='/cafeterias/cafeteria_central.json',
        knowledge_source_name='cafeteria_central',
        verbose=True,
    )

    json_comedor = JSONKnowledgeSource(
        file_paths='/cafeterias/comedor_ual.json',
        knowledge_source_name='comedor',
        verbose=True,
    )

    json_starbucks = JSONKnowledgeSource(
        file_paths='/cafeterias/Starbucks_corners.json',
        knowledge_source_name='maquina_starbucks',
        verbose=True,
    )

    json_aulario_1 = JSONKnowledgeSource(
        file_paths='/aulas/aulario_1.json',
        knowledge_source_name='aulario_1',
        verbose=True,
    )

    json_aulario_2 = JSONKnowledgeSource(
        file_paths='/aulas/aulario_2.json',
        knowledge_source_name='aulario_2',
        verbose=True,
    )

    json_aulario_3 = JSONKnowledgeSource(
        file_paths='/aulas/aulario_3.json',
        knowledge_source_name='aulario_3',
        verbose=True,
    )

    json_aulario_4 = JSONKnowledgeSource(
        file_paths='/aulas/aulario_4.json',
        knowledge_source_name='aulario_4',
        verbose=True,
    )

    json_aulario_5 = JSONKnowledgeSource(
        file_paths='/aulas/aulario_5.json',
        knowledge_source_name='aulario_5',
        verbose=True,
    )

    pdf_biblioteca = PDFKnowledgeSource(
        file_paths='Guia_biblioteca.pdf',
        knowledge_source_name='biblioteca',
        verbose=True,
    )

    json_lunes = JSONKnowledgeSource(
        file_paths='/parking/lunes.json',
        knowledge_source_name='lunes',
        verbose=True,
    )

    json_martes = JSONKnowledgeSource(
        file_paths='/parking/martes.json',
        knowledge_source_name='martes',
        verbose=True,
    )

    json_miercoles = JSONKnowledgeSource(
        file_paths='/parking/miercoles.json',
        knowledge_source_name='miercoles',
        verbose=True,
    )

    json_jueves = JSONKnowledgeSource(
        file_paths='/parking/jueves.json',
        knowledge_source_name='jueves',
        verbose=True,
    )

    json_viernes = JSONKnowledgeSource(
        file_paths='/parking/viernes.json',
        knowledge_source_name='viernes',
        verbose=True,
    )

    json_sabado = JSONKnowledgeSource(
        file_paths='/parking/sabado.json',
        knowledge_source_name='sabado',
        verbose=True,
    )

    json_domingo = JSONKnowledgeSource(
        file_paths='/parking/domingo.json',
        knowledge_source_name='domingo',
        verbose=True,
    )