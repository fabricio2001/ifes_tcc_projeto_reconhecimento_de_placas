$(() => {
  const url = "http://127.0.0.1:5000";

  $('#gridContainer').dxDataGrid({
    dataSource: DevExpress.data.AspNet.createStore({
      key: 'id',
      loadUrl: url + "/Pessoas",
      insertUrl: url + "/Pessoas",
      updateUrl: url + "/Pessoas",
      deleteUrl: url + "/Pessoas",
      onBeforeSend(method, ajaxOptions) {
        ajaxOptions.xhrFields = { withCredentials: false };
      },
    }),
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
        dataField: 'cpf',
        caption: 'Cpf',
        // validationRules: [{ type: 'required' }, {
        //   type: 'pattern',
        //   message: 'O cpf tem que esta no formato "000.000.000-00"!',
        //   pattern: /^\d{3}.\d{3}.\d{3}-\d{2}$/i,
        // }],
        formItem: {
          editorType: 'dxTextBox',
          editorOptions: {
            mask: '000.000.000-00',
          },
        },
      },
      {
        dataField: 'nome',
        caption: 'Nome',
        validationRules: [{ type: 'required' }],
      },
      {
        dataField: 'telefone',
        caption: 'Telefone',
        // validationRules: [{ type: 'required' }, {
        //   type: 'pattern',
        //   message: 'O numero tem que esta no formato "(00) 00000-0000"!',
        //   pattern: /^\(\d{2}\) \d{5}-\d{4}$/i,
        // }],
        formItem: {
          editorType: 'dxTextBox',
          editorOptions: {
            mask: '(00) 00000-0000',
          },
        },
      },
      {
        dataField: 'email',
        caption: 'Email',
        validationRules: [
          { type: 'required' }, 
          { type: 'email',}
        ],
      },
      {
        dataField: 'cargo',
        caption: 'Cargo',
        validationRules: [{ type: 'required' }],
        lookup: {
          dataSource: DevExpress.data.AspNet.createStore({
            key: 'id',
            loadUrl: `${url}/Dados/Cargo`,
            onBeforeSend(method, ajaxOptions) {
              ajaxOptions.xhrFields = { withCredentials: true };
            },
          }),
          valueExpr: 'id',
          displayExpr: 'nome',
        },
      }
    ],
  });
});
