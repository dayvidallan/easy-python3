 function exibir_esconder_campo() {




    if ($('#id_modalidade').val() == 1) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 8.666/93, art. 22, III');
        $("#id_fundamento_legal").prop("readonly", true);
    }

    if ($('#id_modalidade').val() == 2) {
        $('#id_fundamento_legal').val('Fundamento Legal –Lei 8.666/93, art. 22, I');
        $("#id_fundamento_legal").prop("readonly", true);
    }

    if ($('#id_modalidade').val() == 3) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 8.666/93, art. 22, IV');
        $("#id_fundamento_legal").prop("readonly", true);
    }


    if ($('#id_modalidade').val() == 4) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 10.520/06, art. 1°');
        $("#id_fundamento_legal").prop("readonly", true);
    }

    if ($('#id_modalidade').val() == 5) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 8.666/93, art. 22, II');
        $("#id_fundamento_legal").prop("readonly", true);
    }







    if ($('#id_modalidade').val() == 6) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 8.666/93, art. 25, caput');
        $("#id_fundamento_legal").prop("readonly", true);
    }
    if ($('#id_modalidade').val() == 7) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 11.947/09, art. 14, § 1°');
        $("#id_fundamento_legal").prop("readonly", true);
    }
    if ($('#id_modalidade').val() == 8) {
        $('#id_fundamento_legal').val('');
        $("#id_fundamento_legal").prop("readonly", false);
    }
    if ($('#id_modalidade').val() == 9) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 12.188/10, art. 19');
        $("#id_fundamento_legal").prop("readonly", true);
    }



    if ($('#id_modalidade').val() == 10) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 10.520/06, art. 11');
        $("#id_fundamento_legal").prop("readonly", true);
    }
    if ($('#id_modalidade').val() == 11) {
        $('#id_fundamento_legal').val('Fundamento Legal – Lei 8.666/93, art. 15, II e §§ 1º a 6º');
        $("#id_fundamento_legal").prop("readonly", true);
    }

    if ($('#id_tipo').val() == 2) {
        $('#id_tipo_desconto').parent().parent().show();

    }
    else {
        $('#id_tipo_desconto').parent().parent().hide();
        $('#id_tipo_desconto').val('');

    }





 }


  $(document).ready(function() {

    function update_select(select, modalidade) {
		$.ajax({
			method: "GET",
			url: "/busca_tipo_pregao/",
			data: { "modalidade": modalidade },
			success: function(result, textStatus, jqXHR) {
				select.find('option').remove();
				select.append($('<option value="">-------</option>'));
				for (var i in result) {
					select.append($('<option value="'+result[i].pk+'">'+result[i].fields.nome+'</option>'));
				}
			},
			error: function() {
			}
		});
	}

    exibir_esconder_campo();

    $('#id_modalidade').on('change', function(){
        exibir_esconder_campo();
        update_select($('select[name=tipo]'), $('#id_modalidade').val());
    });
    $('#id_tipo').on('change', function(){
        exibir_esconder_campo();
    });
  });
