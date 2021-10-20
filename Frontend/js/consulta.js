
function marcarConsulta () {
	//alert('funcionado');
    let link_backend = "https://pychris.pythonanywhere.com/";



	
    //entrada
	
    var dataConsultaDado = document.getElementById('dataConsulta').value;
   	var motivoConsultaDado = document.getElementById('motivoConsulta').value;
   	let paciente_id_consulta = document.location.search.replace(/^.*?\=/,'');
   	var medico_id_consulta = document.getElementById('selectMedico').value;
    
   	
    
    /*
    //para teste
    let paciente_id_consulta = document.location.search.replace(/^.*?\=/,'');
   	var motivoConsultaDado = "dor no joelho";
   	var dataConsultaDado = "20-10-2021";
   	var medico_id_consulta = 2;
    
    */


	var dados = JSON.stringify({data: dataConsultaDado, motivo: motivoConsultaDado, paciente_id_consulta: paciente_id_consulta, medico_id_consulta: medico_id_consulta});

	$.ajax({
        url : link_backend+'marcar_consulta',
        type : 'POST',
        contentType : 'application/json', // enviando dados em json
        dataType: 'json',
        data: dados,
        success: consultaMarcado,
        error: erroconsultaMarcado
	});


	function consultaMarcado(resposta){
        if (resposta.resultado == "ok") {
            //mensagem
            alert('Consulta marcado com successo!');
            document.location.reload(true);
            //
            
        } else{
            alert(resposta.resultado);

    }
	}
    function erroconsultaMarcado(resposta){
        alert("Erro na comunicação com o backend");
    }

}