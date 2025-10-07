

addEventListener('DOMContentLoaded', () =>{

// Quiz der die das
    function sendreq()
    {
        fetch('menu/api/words')
        .then(response => response.string())
        .then(Wort => {
            console.log(Wort));
        }
        getElementById('Empfenger').innerHTML = Wort;
    }


addEventListener('click', (event) =>
    {
        if (event.target.id == 'senreq')
        {
            sendreq();
        }
    });




});