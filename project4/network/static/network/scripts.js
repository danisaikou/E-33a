
// Run scripts after content of page fully loaded 

document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#all_posts').style.display = 'block';
    
    create_post();
    load_posts('all');
});

function create_post() {
    document.querySelector('#post_content').value = '';

    document.querySelector('#create_post').onsubmit = function() {
        let content = document.querySelector('#post_content').value;
        fetch('/create_post', {
            method: 'POST', 
            body: JSON.stringify({
                content: content
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(`It worked?: ${data}`);
        });
    }
}

function load_posts(user) {
    let post_block = document.createElement('div');
    post_block.id = 'post_block';


}

