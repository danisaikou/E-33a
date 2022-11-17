document.addEventListener('DOMContentLoaded', function() {

    like = document.querySelectorAll('.liked');
    like.forEach((element) => {
        like_func(element);
    });

    function like_func(x) {
        x.classList.toggle("fa-heart").css('color','#df4759');
    }
}
// Edit
// LIsten for clicks
// document.addEventListener('click', event => {
//     const element = event.target;

//     // If edit clicked
//     if (element.dispatchEvent.startsWith('edit_')) {
//         const edit_button = element;
//         const post_id = edit_button.dataset.id;
//         const post_text = document.getElementById(`post_content_${post_id}`)

//         let text_area = document.createElement('textarea');
//         text_area.innerHTML = post_text.innerHTML;
//         text_area.id = `textarea_${post_id}`;
//         text_area.className = 'form-control';
//         document.getElementById(`post_contentgroup_${post_id}`).append(text_area)

//         // hide edit
//         edit_button.style.display = 'none';

//         // add save
//         const save_button = document.createElement('button');
//         save_button.innerHTML = 'Submit';
//         save_button.className = 'btn btn-danger';
//         save_button.id = `save_${post_id}`
//         document.getElementById(`save_button_${post_id}`).append(save_button);
//         save_button.addEventListener('click', function() {
//             text_area = document.getElementById(`textarea_${post_id}`);

//             //fetch to update page 
//             fetch(`/editpost/${post_id}`, {
//                 method: 'POST',
//                 body: JSON.stringify({
//                     content: text_area.value,
//                 })
//             })
//             .then (response => {
//                 if (response.ok || response.status == 400) {
//                     return response.json()
//                 } 
//             })
//             .catch(error => {
//                 console.error(error);
//             })
//         })

//         }
//     })
// })