window.jsPDF = window.jspdf.jsPDF;

$(() => {
    const url = "http://127.0.0.1:5000";

    $('#gridContainer').dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: 'id',
            loadUrl: url + "/Registros",
            insertUrl: url + "/Registros",
            updateUrl: url + "/Registros",
            deleteUrl: url + "/Registros",
            onBeforeSend(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: false };
            },
        }),
        selection: {
            mode: 'multiple',
        },
        columnsAutoWidth: true,
        showBorders: true,
        rowAlternationEnabled: true,
        filterRow: {
            visible: true,
            applyFilter: 'auto',
        },
        searchPanel: {
            visible: true,
            width: 240,
            placeholder: 'Pesquisa...',
        },
        headerFilter: {
            visible: true,
        },
        paging: {
            pageSize: 10,
        },
        pager: {
            visible: true,
            allowedPageSizes: [5, 10, 20],
            showPageSizeSelector: true,
            showInfo: true,
            showNavigationButtons: true,
        },
        editing: {
            mode: 'form',
            allowUpdating: false,
            allowAdding: true,
            allowDeleting: false,
        },
        columns: [
            {
                dataField: 'placa',
                caption: 'Placa',
                validationRules: [{ type: 'required' }, {
                    type: 'pattern',
                    message: 'A placa tem que esta no formato "AAA0A00"!',
                    pattern: /^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$/i,
                }],
            },
            {
                dataField: 'direcao',
                caption: 'Direcao',
                validationRules: [{ type: 'required' }],
                lookup: {
                    dataSource: states,
                    displayExpr: 'Name',
                    valueExpr: 'ID',
                },
            }
            ,
            {
                dataField: 'tipo',
                value: 1,
                caption: 'Origrm do Cadastro',
                lookup: {
                    dataSource: typeCad,
                    displayExpr: 'Name',
                    valueExpr: 'ID',
                },
                formItem: {
                    disabled: true,
                },
            },
            {
                dataField: 'data',
                caption: 'Data',
                validationRules: [{ type: 'required' }],
                dataType: 'datetime',
                format: 'dd/MM/yyyy HH:mm:ss',
                sortIndex: 1, sortOrder: "desc",
                value: new Date(),
            }
        ],
        export: {
            enabled: true,
            formats: ['pdf'],
            allowExportSelectedData: true,
        },
        onExporting(e) {
            const doc = new jsPDF();

            DevExpress.pdfExporter.exportDataGrid({
                jsPDFDocument: doc,
                component: e.component,
                indent: 5,
            }).then(() => {
                doc.save('Registros.pdf');
            });
        },
    });
});

const states = [{
    ID: 1,
    Name: 'Entrando',
}, {
    ID: 2,
    Name: 'Saindo',
}];

const typeCad = [{
    ID: 1,
    Name: 'Manual',
}, {
    ID: 2,
    Name: 'Sistema',
}];