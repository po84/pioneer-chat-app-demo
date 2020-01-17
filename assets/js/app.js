let socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
	socket.emit('chat_event', {
		data: 'User Connected'
	});
	let form = $('form').on('submit', function(e) {
		e.preventDefault();

		let username = $('select#username').val();
		let msgText = $('input#message_text').val();

		socket.emit('chat_event', {
			username: username,
			message: msgText
		});

		$('input#message_text').val('').focus();
	});
});

socket.on('server_response', function(msg) {
	console.log(msg);
	if (typeof msg.username !== 'undefined') {
		$('div#message_holder').append('<div>' + msg.username + ': ' + msg.message + '</div>');
	}
});
