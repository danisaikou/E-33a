// Run script after content of page fully loaded
document.addEventListener('DOMContentLoaded', function() {

	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', compose_email);

	// Listen for when user submits the compose form to send an e-mail 
	document.querySelector('#compose-form').addEventListener('submit', send_email);

	// By default, load the inbox
	load_mailbox('inbox');
});


function compose_email() {

	// Show compose view and hide other views
	document.querySelector('#email-view').style.display = 'none';
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';

	// Clear out composition fields
	document.querySelector('#compose-recipients').value = '';
	document.querySelector('#compose-subject').value = '';
	document.querySelector('#compose-body').value = '';

}

function view_email(id) {

	// Fetch emails using /emails/<email_id>
	fetch(`/emails/${id}`)
		.then(response => response.json())
		.then(email => {
			// Print email to console
			console.log(email);

			// ... do something else with email ...
			// Hide things we don't need to look at 
			document.querySelector('#emails-view').style.display = 'none';
			document.querySelector('#compose-view').style.display = 'none';
			document.querySelector('#email-view').style.display = 'block';

			// HTML the single email view 
			document.querySelector('#email-view').innerHTML = `
    <table class="email-table">
      <thead>
        <tr class="table-light">
          <th><h3>${email.subject}</h3></th>
        </tr>
      </thead>

      <tbody>
        <tr class="table-secondary">
          <td>
          <strong>From: </strong>${email.sender} <br> 
          <strong>To: </strong>${email.recipients} <br>
          <em>${email.timestamp}</em>
          </td>
        </tr>
        <tr class="table-email-body">
          <td>
            <blockquote class="blockquote">${email.body}</blockquote>
          </td>
        </tr>
      </tbody>
    </table>
    `;

			// Check if not read and udpate when it is read
			if (!email.read) {
				fetch(`/emails/${id}`, {
					method: 'PUT',
					body: JSON.stringify({
						read: true
					})
				});
			}

			// Reply moved above archive for button positioning purposes 
			const reply_btn = document.createElement('button');
			reply_btn.innerHTML = "Reply";
			reply_btn.className = "btn btn-primary";
			reply_btn.addEventListener('click', function() {
				compose_email();

				document.querySelector('#compose-recipients').value = email.sender;

				document.querySelector('#compose-subject').value = `${email.subject}`.includes("RE:") ? `${email.subject}` : `RE: ${email.subject}`;
				document.querySelector('#compose-body').value = `\n \n >>>>> \n On ${email.timestamp}, ${email.sender} wrote: \n ${email.body}`;

			});

			// Append a button to the bottom of the single email view screen 
			document.querySelector('#email-view').append(reply_btn);


			// Archive / Un-archive 
			const archive_btn = document.createElement('button');
			archive_btn.innerHTML = email.archived ? "Un-archive" : "Archive";
			archive_btn.className = "btn btn-dark";
			archive_btn.addEventListener('click', function() {
				console.log('This element has been clicked!');

				// Send a PUT request to /emails/<email_id> to mark an email as archived or un-archived
				fetch(`/emails/${id}`, {
						method: 'PUT',
						body: JSON.stringify({
							archived: !email.archived
						})
					})
					.then(() => {
						load_mailbox('inbox')
					});

			});
			// Append a button to the bottom of the single email view screen 
			document.querySelector('#email-view').append(archive_btn);


		});
}

function load_mailbox(mailbox) {

	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'block';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-view').style.display = 'none';

	// Show the mailbox name
	document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

	// Make a GET request to /emails/inbox, convert response into JSON, and provide the array of emails inside of the variable emails
	fetch(`/emails/${mailbox}`)
		.then(response => response.json())
		.then(emails => {
			// For each email create div 
			emails.forEach(one => {
				const email = document.createElement('div');
				email.innerHTML = `
      <table>
        <tbody>
          <tr>
            <td><strong>${one.timestamp}</strong></td> 
            <td><strong>From: </strong>${one.sender}</td>
            <td><strong>Subj: </strong>${one.subject}</td>
          </tr>
        </tbody>
      </table>
      `;

				// Set read emails to grey bkg
				email.className = one.read ? 'read' : 'new';

				email.addEventListener('click', function() {
					view_email(one.id);
				});

				document.querySelector('#emails-view').append(email);
			});
		});
}

function send_email(event) {
	event.preventDefault();
	console.log('working');

	document.querySelector('#email-view').style.display = 'none';

	const recipients = document.querySelector('#compose-recipients').value;
	const subject = document.querySelector('#compose-subject').value;
	const body = document.querySelector('#compose-body').value;

	// Send e-mail using POST request to /emails route and return status code/ JSON response passing in values for recip/subj/body
	fetch('/emails', {
			method: 'POST',
			body: JSON.stringify({
				recipients: recipients,
				subject: subject,
				body: body
			})
		})
		.then(response => response.json())
		.then(result => {
			// Print result to the console 
			console.log(result);
			load_mailbox('sent');
		});
	return false;
}