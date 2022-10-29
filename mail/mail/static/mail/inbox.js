document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

// Make GET request to /emails/<mailbox> to request mail for a particular mailbox
//TODO 

// Make GET request to /emails/<email_id> to request email
function view_email() {
  fetch(`/emails/${emails}`)
  .then(response => response.text())
  .then(text => {
    console.log(text);
    document.querySelector('#emails-view').innerHTML = text;
  });
}


function view_email() {
  // Show mailbox without detail / composing views 
  document.querySelector('#emails.view').style.display = "block";
  document.querySelector('#emails-detail').style.display = "none";
  document.querySelector('#compose-view').style.display = "none";
}
  // Fetch mail 
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    console.log(emails);
    emails.array.forEach(email => show_email(email, mailbox))
  });


function send_email() {
  const recipients = document.querySelector('#compose-recipients').value; // comma-separated string of users 
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;
  console.log(recipients);

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
  });
  return false;
}
load_mailbox('sent');

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch the most recent emails 
  fetch(`/emails/${mailbox}`)
  

}