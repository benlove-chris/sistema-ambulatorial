
function marcarConsulta () {
	//alert('funcionado');
    let link_backend = "http://localhost:5000/";



	
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


//---------------marcar exame---------------------



function marcarExame(){
  
  //alert('funcionado');
    let link_backend = "http://localhost:5000/";



  
    //entrada
    var dataExame = document.getElementById('dataExame').value;
    var tipoExame = document.getElementById('tipoExame').value;
    var resultado_exame = document.getElementById('resultadoExame').value;
    

    let paciente_id_exame = document.location.search.replace(/^.*?\=/,'');
    var consulta_id_exame = document.getElementById('dataSolicitacao').value;
    var medico_id_exame = document.getElementById('selectMedicoSolicitante').value;
    



    var dados = JSON.stringify({dataExame: dataExame, tipoExame: tipoExame, resultado_exame: resultado_exame, 
      paciente_id_exame: paciente_id_exame, consulta_id_exame: consulta_id_exame, medico_id_exame:medico_id_exame});

    console.log(dados);




  $.ajax({
        url : link_backend+'marcar_exame',
        type : 'POST',
        contentType : 'application/json', // enviando dados em json
        dataType: 'json',
        data: dados,
        success: exameMarcado,
        error: erroexameMarcado
  });


  function exameMarcado(resposta){
        if (resposta.resultado == "ok") {
            //mensagem
            alert('Exame marcado com successo!');
            document.location.reload(true);
            //
            
        } else{
            alert(resposta.resultado);

    }
  }
    function erroexameMarcado(resposta){
        alert("Erro na comunicação com o backend");
    }

}
