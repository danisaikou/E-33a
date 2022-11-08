let counter = 1;
const quantity = 10;

// Run scripts after content of page fully loaded 

document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
	document.querySelector('#all_posts').addEventListener('click', () => load_network ('all_posts'));
	
    document.querySelector('#profile').addEventListener('click', () => load_network ('profile'));
	
    document.querySelector('#following').addEventListener('click', () => load_network ('following'));
	
    document.querySelector('#create').addEventListener('click', create_post);

	// Listen for when user submits the compose form to send an e-mail 
	document.querySelector('#PostForm').addEventListener('submit', create_post);

	// By default, load the inbox
	load_network('all_posts');
}); 

function load_network() {
    
}

function create_post() {

}

