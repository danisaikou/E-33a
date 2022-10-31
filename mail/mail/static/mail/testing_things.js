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
 
  