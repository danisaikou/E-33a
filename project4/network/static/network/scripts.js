let counter = 1;
const quantity = 10;

// Run scripts after content of page fully loaded 

document.addEventListener('DOMContentLoaded', function() {

    // Use buttons for New Post, All Posts, Following, and Log In/Out
	document.querySelectorAll("div.post").forEach((postNode) => {
        updateLikes(postNode);
    });

    // Like button 
    // Animation src https://mojs.github.io/tutorials/getting-started.html#setup-mo-js-in-your-project
    // var elem = document.querySelector('.heart');
    // elem.addEventListener('click', function(e) {
    //     this.classList.add('hidden');
    // const heart = new mojs.Shape({
    //     parent: elem,
    //     shape: 'heart',
    //     fill: '#ab0039',
    //     scale: {0: 1.0},
    //     easing: 'elastic.out',
    //     fill: {'pink': 'red'},
    //     duration: 1000,
    //     dleay: 300,
    //     radius: 20 
    // })
    // const circle = new mojs.Shape ({
    //     parent: elem,
    //     shape: 'circle',
    //     stroke: '#ab0039',
    //     strokeWidth: {10: 0},
    //     fill: 'none',
    //     scale: {0 : 1},
    //     radius: 40,
    //     duration: 400,
    //     easing: 'cubic.out',
    //     delay: 300
    // })

    // const burst = new mojs.Burst ({
    //     parent: elem,
    //     radius: {4 : 40},
    //     angle: 45,
    //     count: 14,
    //     timeline: {delay: 400},
    //     children: {
    //         radius: 3,
    //         fill: '#ed0552',
    //         scale: {1 : 0, easing: 'quad.in'},
    //         pathScale: [.8, null],
    //         degreeShift: [300, null],
    //         duration: [500, 700],
    //         easing: 'quint.out'
    //     }
    // })
    // let timeline = new mojs.Timeline();
    // timeline.add(heart, circle, burst)

    // elem.addEventListener('click', function(e) {
    //     this.classList.add('hidden');
    //     timeline.replay()
    // })

