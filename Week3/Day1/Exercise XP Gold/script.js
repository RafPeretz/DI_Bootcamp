let allBooks = ["lesMiserables", "leRougeEtLeNoir", "BelAmi"];

let lesMiserables = 
{
	title: 'Les Misérables',
	author: 'Victor Hugo',
	image: 'https://images-na.ssl-images-amazon.com/images/I/81SGVhaL+dL.jpg',
	alreadyRead : true
};

let leRougeEtLeNoir = 
{
	title: 'Le Rouge et le Noir',
	author: 'Stendhal',
	image: 'https://images-na.ssl-images-amazon.com/images/I/71MA4dKZrRL.jpg',
	alreadyRead : false
};


let BelAmi = 
{
	title: 'Bel-Ami',
	author: 'Maupassant',
	image: 'https://images-na.ssl-images-amazon.com/images/I/61fGVP0W0bL.jpg',
	alreadyRead : true
};


let btnGet = document.querySelector('button');
let myTable = document.querySelector('#table');

btnGet.addEventListener('click', () => {
    let table = document.createElement('table');
    let headerRow = document.createElement('tr');
    headers.forEach(headerText => {
        let header = document.createElement('th');
        let textNode = document.createTextNode(headerText);
        header.appendChild(textNode);
        headerRow.appendChild(header);
    });
    table.appendChild(headerRow);
    employees.forEach(emp => {
        let row = document.createElement('tr');
        Object.values(emp).forEach(text => {
            let cell = document.createElement('td');
            let textNode = document.createTextNode(text);
            cell.appendChild(textNode);
            row.appendChild(cell);
        })
        table.appendChild(row);
    });
    myTable.appendChild(table);
});
