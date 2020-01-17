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

	let answeringButton = $('button#answer_question_btn').click(function(e) {
		e.preventDefault();

		let userId = $('select#username').val();
		let msgText = $('input#message_text').val();
		let questionId = $('input#question_id').val();

		socket.emit('answer_event', {
			user_id: userId,
			message: msgText,
			question_id: questionId
		});

		$('input#message_text').val('').focus();
		$('input#question_id').val('');
		$('div#default_btn_group').removeClass('hidden');
		$('div#answering_btn_group').addClass('hidden')
	});

	let cancelAnsweringButton = $('button#cancel_answering_btn').click(function(e) {
		e.preventDefault();

		$('input#question_id').val('');
		$('div#default_btn_group').removeClass('hidden');
		$('div#answering_btn_group').addClass('hidden')
	});
});

socket.on('server_response', function(msg) {
	if (typeof msg.username !== 'undefined') {
		let newMessageElement = $('<div>' + msg.username + ': ' + msg.message + '</div>')
		if (msg.question_id) {
			let questionId = msg.question_id;

			newMessageElement.click(function(e) {
				e.preventDefault();
				console.log("you can answer this: " + questionId);
				$('input#question_id').val(questionId);
				$('div#default_btn_group').addClass('hidden');
				$('div#answering_btn_group').removeClass('hidden')
			});

			newMessageElement.addClass('is-question');

		} else if (msg.answer_id) {
			let questionId = msg.question_id;

			newMessageElement.addClass('is-answer');
			
		}

		$('div#message_holder').append(newMessageElement);
	}
});
