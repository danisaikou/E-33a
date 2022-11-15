function like(id) {
    const like_btn = document.getElementById("liked").style.visibility = 'hidden';
    const not_liked_btn = document.getElementById("not_liked").style.visibility = 'visible';

    like_btn.addEventListener('click', function onClick() {
       // update frm hidden to visible
       if (like_btn.style.visibility === 'hidden') {
            fetch(`/like/` + id, {
                method: 'PUT',
                body: JSON.stringify({
                    like: true
                })
            })
            
            like_btn.style.visibility = 'visible';

            fetch(`/like/` + id, {
                method: 'PUT',
                body: JSON.stringify({
                    like: false
                })
            })
            
            like_btn.style.visibility = 'hidden';

            fetch(`/like/` + `${id}`) 
                .then(response => response.json())
                .then(post => {
                    like_count.innerHTML = post.likes;
                });
            }
            return false;
      });
}



