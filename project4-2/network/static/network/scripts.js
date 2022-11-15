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



