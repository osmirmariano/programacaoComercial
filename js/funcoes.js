function minhaFuncao1() {
    $('#area-01').css({
        color: '#ff0000',
        textTransform: 'uppercase',
        width: '70%'
    });
};

function minhaFuncao2(){
    $('#area-02').empty();

    var alunos = ['Aluno 01', 'Aluno 02', 'Aluno 03', 'Aluno 04', 'Aluno 05'];
    
    $.each(alunos, function(index, value){
        $('#area-02').append(value);
    });
};

function minhaFuncao3(){
    $('#area-02').empty();

    var alunos = [
        {
            nome: 'Aluno 1',
            idade: 11
        },
        {
            nome: 'Aluno 2',
            idade: 22
        },
        {
            nome: 'Aluno 3',
            idade: 33
        },
        {
            nome: 'Aluno 4',
            idade: 44
        },
        {
            nome: 'Aluno 5',
            idade: 55
        }
    ];

    for(x=0; x<5; x++){
        console.log(alunos[x]);
    }

    var list = $("#area-02").append('<ul></ul>').find('ul');
    $.each(alunos, function(index, value){
        list.append('<li>'+ value.nome + ' - ' + value.idade + '</li>');
    });
};