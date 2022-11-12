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

function load_network(posts) { 

    if (posts.includes("?")) {
        addon = `&page=${page}`;
    } 
    else {
        document.quertySelector('#profile')
        addon = `?page=${page}`
    }

    // Make a GET request to /emails/inbox, convert response into JSON, and provide the array of emails inside of the variable emails
	console.log(`access ${addon}`);
    fetch(`/load${addon}`)
    .then(response => response.json())
    .then(resposne => {
        document.getElementById('posts').innerHTML=
            `
            <strong>{post.user_id} ·</strong>
            <small><i>{post.datetime}</i></small>
            <p>{post.content}</p>
            <strong>{post.likes}</strong> Like(s)
            `;
        resposne.posts.forEach(post => build_post(post));
            })
    }

function create_post() {


}

