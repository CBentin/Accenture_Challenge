
let residentes = {
	info: [
		{
			placa: '749-WCX',
			nombre: 'Alonso'
		},
		{
			placa: 'RKT-089-A',
			nombre: 'Alberto'
		},
		{
			placa: 'STW-36-05',
			nombre: 'Carlos'
		}
	], json:true
};


let visitantes = {
	info:[
		{
			placa: 'RJ-80-167'
		},
		{
			placa: 'SLB-49-08'
		}
	], json:true
};

for(let i = 1; i <=1016; i++){
    getFrame(i, function(img, placa){
        let base64img = getBase64Img(img);
        console.log(placa);
        displayInfo(base64img, placa);
    });
}

function getFrame(val, callback){    
    $.ajax({
        url: "http://localhost:8080/getFrame",
        data:{
            count: val
        },
        method: "GET",
        dataType: "json",
        success: function (responseJSON){
            let base64img = responseJSON.image
            let plate = responseJSON.plate
            callback(base64img, plate);
        }
    });
}

function displayInfo(img64, placa){
	let info = document.getElementById('info');
	let small = document.getElementById('small');

	for(let i = 0; i < residentes.info.length; i++){

		if(placa == residentes.info[i].placa){
            $('#main').html('');
            Base64ToImage(img64, function(img){
			    document.getElementById('main').appendChild(img);
			});
			
			info.innerText = "Bienvenido(a) " + residentes.info[i].nombre;
            small.innerText = placa;
            
            break;
		}
	}

	for(let i = 0; i < visitantes.info.length; i++){
		if(placa == visitantes.info[i].placa) {
            $('#main').html('');
            Base64ToImage(img64, function(img) {
                document.getElementById('main').appendChild(img);
            });

			info.innerText = "Bienvenido(a) Visitante!";
            small.innerText = placa;
            
            break;
		}
    }
    /*$('#main').html('');
    Base64ToImage(img64, function(img) {
        document.getElementById('main').appendChild(img);
    });*/
	//info.innerText = "ACCESO DENEGADO!";

}

function Base64ToImage(base64img, callback) {
    var img = new Image();
    img.onload = function() {
        callback(img);
    };
    img.src = base64img;
    
}


function getBase64Img(img) {
    return "data:image/png;base64,"+img;
}