/*
$.ajax({
    url: 'http://localhost:5000/listar_paciente/1',
    method: 'GET',
    dataType: 'json',
    success: console.log('as'),//listar_paciente,

    error: function(){
        alert("Erro ao ler os dados :) \nverifique o backend");}
});

	


*/


function listarDadosPaciente(){
	//alert("especifica");
	let id_paciente = document.location.search.replace(/^.*?\=/,'');
	$.ajax({
		url: 'http://localhost:5000/listar_paciente/'+id_paciente,
		method: "GET",
        dataType: "json",
		success: listar_paciente,

        error: function(){
            alert("Erro ao ler os dados :) \nverifique o backend 1");
        }



	});
	//if (Status === 444){}
}



function listar_paciente(paciente){
	$("#nome-paciente").text(paciente.nome + " "+paciente.sobrenome) 
	
	console.log(paciente.nome);
	linha = 	'<tr>'+
        		"<td>" + paciente.nome+ "</td>" + 
            	"<td>" + paciente.sobrenome+ "</td>" + 
            	"<td>" + paciente.id_paciente+ "</td>" + 
    		'</tr>'
	
	
	$("#corpoDados").html(linha);

}

//Consulta
function listarDadosConsulta(){
	let id_paciente = document.location.search.replace(/^.*?\=/,'');
	$.ajax({
		url: 'http://localhost:5000/listar_consulta/'+id_paciente,
		method: "GET",
        dataType: "json",
		success: listar_consulta,

        error: function(){
            alert("Erro ao ler os dados :) \nverifique o backend 1");
        }



	});
	//if (Status === 444){}
}

function listar_consulta(paciente) {
	//$("#nome-paciente").text(paciente.nome + " "+paciente.sobrenome) 
	
	console.log(paciente.data);
	linhas = ""
	//console.log(consultas);

	for (var consulta in paciente){
		console.log(paciente[consulta].data);
		//console.log(consulta.data);
		lin = 	'<tr>'+
	        		"<td>" + paciente[consulta].data+ "</td>" + 
	        		"<td>" + paciente[consulta].medico.nome+ "</td>" + 
	        		"<td>" + paciente[consulta].motivo+ "</td>" + 
	    		'</tr>'

	    linhas += lin;
	}
	
	
	$("#corpoConsulta").html(linhas);

}