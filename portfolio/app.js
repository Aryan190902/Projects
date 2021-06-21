content = [
    {
        name: 'Home'
    },
    {
        name: 'Projects'
    },
    {
        name: 'Education'
    }
];
const data = document.querySelector('.ul')

function info(item)
{
    return '<div>' + item.name + '</div>';
};
let contents = content.map(info);
ul.innerHTML = contents.join('\t');