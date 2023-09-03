$(() => {
    $('#gridContainer').dxDataGrid({
        dataSource: "http://127.0.0.1:5000/json",
        keyExpr: 'ID',
        showBorders: true,
        paging: {
            enabled: false,
        },
        editing: {
            mode: 'form',
            allowUpdating: true,
            allowAdding: true,
            allowDeleting: true,
        },
        columns: [
            {
                dataField: 'nome',
                caption: 'Nome',

            },
            {
                dataField: 'endereco',
                caption: 'Endereco',

            }
        ],
    });
});
