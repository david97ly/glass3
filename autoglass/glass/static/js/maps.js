
$(function() {
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(getCoords,getError);
		
	}else{
		  initialize(13.7761745,-90.0330749);	
	}
	
	function getCoords(position) {
		var lat = position.coords.latutude;
		var lng = Position.coords.longitude;
		
		initialize(lat,lng);
	}
	
	function getError(err) {
         initialize(13.7761745,-90.0330749);		
	}
	
	function initialize(lat,lng) {
		var latlng = new google.maps.LatLng(lat,lng);
		var mapSettings = {
			center:latlng,
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		
		map = new google.maps.Map($('#mapa').get(0), mapSettings);
		var marker = new google.maps.Marker({
			position: latlng,
			map: map,
			draggable:true,
			title: 'Arrastrar'
		});
	}
	
});