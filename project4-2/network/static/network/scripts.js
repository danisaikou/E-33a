function like(post_id) {
    let post_div = document.getElementById(`${post_id}`);
    let like_div = post_div.querySelector("#likes");
    let count = like_div.querySelector("#count");
    let likes = parseInt(count.getAttribute('value'), 10);

    fetch(`/like`, {
        method: "POST", 
        body: JSON.stringify ({
            post_id: post_id,
        })
    })
    .then(async(response) => {
        if (response.status === 201) {
            like_div.querySelector('#liked').style.display = 'inline-block';
            like_div.querySelector('#not_liked').style.display = 'none';

            count.innerHTML = likes + 1
            console.log('Liked');
        }

        else {
            throw new Error(msg.error);
        }
    })

    .catch(error => {
        console.log('Error');
    });
    return false;
    }

function save(post_id) {
    let post_div = document.getElementById(`${post_id}`);
    let post = post_div.querySelector(`#post`)

    let new_post = post.querySelector('texatarea.new_post').value();

    console.log(new_post)

    fetch (`/edit/${post_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            body: new_post,
        })
    })

    .then(async(response) => {
        if (response.status == 201) {
            post_div.querySelector('#edit').style.display = "block";
            post_div.querySelector('#save').style.display = 'none';
            new_post.innerHTML = `${new_post}`;
            console.log(`Edited.`)
        }

        else {
            throw new Error(msg.error)
        }
    })
    .catch(error => {
        console.log('Error: ', error);
    });
    return false;
}


