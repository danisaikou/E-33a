// Run script after content of page fully loaded
document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));

  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));

  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Listen for when user submits the compose form to send an e-mail 
  document.querySelector('#compose-form').addEventListener('submit', send_email)

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(reply=false) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  if (!reply) {
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
} else {
  subject = `RE: ${subject}`;
  document.querySelector('#compose-recipients').value = str(recipents);

}
}


function send_email(event) {
  event.preventDefault
  console.log('is this working? yes');
  const recipients = document.querySelector('#compose-recipients').value; // comma-separated string of users 
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;
  
  // Send e-mail using POST request to /emails route and return status code/ JSON response passing in values for recip/subj/body
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: 'recipients', 
        subject: 'subject', 
        body: 'body'
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result to the console 
      console.log(result);
      load_email('sent');
  });
  return false;
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}

