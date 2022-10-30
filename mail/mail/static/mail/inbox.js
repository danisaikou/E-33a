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
  subject = `RE: ${'#compose-subject'}`;

}
}

function view_email(id) {
  // Get individual emails to display using ID 
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    // Print email
    console.log(email);
    
    // ... do something else with email ...
    // Hide things we don't need to look at 
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-view').style.display = 'block';
    
    // HTML the single email view 
    document.querySelector('#email-view').innerHTML = `mail display`;

});
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

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
      <strong>${one.timestamp} </strong> |
      <strong>Sender: </strong>${one.sender} |  
      <strong>Subj: </strong>${one.subject} 
      </label>
      `;
      
      // Set read emails to grey bkg
      email.className = one.read ? 'read': 'new';
      
      email.addEventListener('click', function() {
        view_email(one.id)
      });

      document.querySelector('#emails-view').append(email);
      })
  });
  }



function send_email(event) {
  event.preventDefault();
  console.log('working');
  
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