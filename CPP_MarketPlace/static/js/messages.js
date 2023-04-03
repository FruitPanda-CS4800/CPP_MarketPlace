let input_message = $('#input-message')
let message_body = $('.msg_card_body')
let send_message_form = $('#send-message-form')
const USER_ID = $('#logged-in-user').val()

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'https') {
    wsStart = 'ws://'
}

let endpoint = wsStart + loc.host + loc.pathname

//let endpoint = wsStart + location.pathname
var socket = new WebSocket(endpoint)
console.log(endpoint)

socket.onopen = async function(e){
    console.log('open', e)

    send_message_form.on('submit', function(e){
        e.preventDefault()
        let message = input_message.val()
        let send_to;
        if(USER_ID == 1)
            send_to = 2
        else
            send_to = 1
        let data = {
            'message': message,
            'sent-by': USER_ID,
            'send_to': send_to
        }
        data = JSON.stringify(data)
            socket.send(data)
            $(this)[0].reset()
    })
}

socket.onmessage = async function(e){
    console.log('message', e)
    let data = JSON.parse(e.data)
    let message = data['message']
    let sent_by_id = data['sent_by']
    newMessage(message, sent_by_id)
}

socket.onerror = async function(e){
    console.log('error', e)
}

socket.onclose = async function(e){
    console.log('close', e)
    console.log(e.code)
}

function newMessage(message, sent_by_id) {
    if($.trim(message) === '') {
        return false;
    }
    let message_element;
    if(sent_by_id == USER_ID){
    message_element =
    `<div class="d-flex mb-4 replied">
        <div class="msg_cotainer_send">
            ${message}
            <span class="msg_time_send"> 8:55 AM, Today </span>
        </div>
        <div class="img_cont_msg">
            <img src=""></img>
        </div>
    </div>`
    }
    else{
        message_element = `
        <div class="d-flex mb-4 received">
								<div class="img_cont_msg">
									<img src="https://static.turbosquid.com/Preview/001292/481/WV/_D.jpg" class="rounded-circle user_img_msg">
								</div>
								<div class="msg_cotainer">
									${message}
									<span class="msg_time">8:40 AM, Today</span>
								</div>
							</div>
                            `
    }

    message_body.append($(message_element))
    message_body.animate({
        scrollTop: $(document).height()
    }, 100)
    input_message.val(null);
}
