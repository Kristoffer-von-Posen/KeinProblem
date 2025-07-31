

// Quiz der die das

function DerDieDas(x)
{
    if (x == 1)
    {
        alert("Correct");
    }
    else
    {
        alert("Incorrect");
    }
}

function showWords(day, week)
    {
        const words = document.querySelectorAll('.words');
        words.forEach(word => {
            if ((word.dataset.day == day || day=="all") && word.dataset.week == week) {
                word.style.display = 'block';
            } else {
                word.style.display = 'none';
            }
        });
    }

document.addEventListener('DOMContentLoaded', () =>
    {
        
        showWords(1, 1);
        
        document.getElementById('GO').addEventListener('click', () => {let x = document.getElementById('Day').value;
    let y = document.getElementById('Week').value;
        showWords(x, y);}
            );
      
        
    })