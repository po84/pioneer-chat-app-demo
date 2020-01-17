let socket = io.connect('http://' + document.domain + ':' + location.port);

$.ajax({
	type: "GET",
	url: "/users",
	success: function(result, status, xhr) {
		let userSelect = $('select#username');
			result.output.forEach(user => {
			userSelect.append('<option value="' + user.id + '">' + user.display_name + '</option>');
		});
	}
	
});

socket.on('connect', function() {
	socket.emit('connected_event', {
		data: 'User Connected'
	});
	let form = $('form').on('submit', function(e) {
		e.preventDefault();

		let userId = $('select#username').val();
		let msgText = $('input#message_text').val();

		socket.emit('chat_event', {
			user_id: userId,
			message: msgText
		});

		$('input#message_text').val('').focus();
	});

	let askQuestionButton = $('button#ask_question_btn').click(function(e) {
		e.preventDefault();

		let userId = $('select#username').val();
		let msgText = $('input#message_text').val();
		socket.emit('question_event', {
			user_id: userId,
			message: msgText
		});

		$('input#message_text').val('').focus();
	});
});

socket.on('server_response', function(msg) {
	console.log(msg);
	if (typeof msg.username !== 'undefined') {
		let newMessageElement = $('<div>' + msg.username + ': ' + msg.message + '</div>')
		if (msg.question_asked) {
			newMessageElement.click(function(e) {
				e.preventDefault();
				console.log("you can answer this");
			});
			newMessageElement.addClass('is-question');
		}
		$('div#message_holder').append(newMessageElement);
	}
});
