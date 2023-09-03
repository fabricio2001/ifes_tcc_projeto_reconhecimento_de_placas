$(() => {
  const url = "http://127.0.0.1:5000";

  $('#gridContainer').dxDataGrid({
    dataSource: DevExpress.data.AspNet.createStore({
      key: 'id',
      loadUrl: url + "/Carros",
      insertUrl: url + "/Carros",
      updateUrl: url + "/Carros",
      deleteUrl: url + "/Carros",
      onBeforeSend(method, ajaxOptions) {
        ajaxOptions.xhrFields = { withCredentials: false };
      },
    }),
    columnsAutoWidth: true,
    rowAlternationEnabled: true,
    showBorders: true,
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
        dataField: 'placa',
        caption: 'Placa',
        // validationRules: [{ type: 'required' }],
        validationRules: [{ type: 'required' }, {
          type: 'pattern',
          message: 'A placa tem que esta no formato "AAA0A00"!',
          pattern: /^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$/i,
        }],
      },
      {
        dataField: 'modelo',
        caption: 'Modelo',
        validationRules: [{ type: 'required' }],
        lookup: {
          dataSource: DevExpress.data.AspNet.createStore({
            key: 'id',
            loadUrl: `${url}/Dados/Modelo`,
            onBeforeSend(method, ajaxOptions) {
              ajaxOptions.xhrFields = { withCredentials: true };
            },
          }),
          valueExpr: 'id',
          displayExpr: 'nome',
        },
      },
      {
        dataField: 'marca',
        caption: 'Marca',
        validationRules: [{ type: 'required' }],
        lookup: {
          dataSource: DevExpress.data.AspNet.createStore({
            key: 'id',
            loadUrl: `${url}/Dados/Marca`,
            onBeforeSend(method, ajaxOptions) {
              ajaxOptions.xhrFields = { withCredentials: true };
            },
          }),
          valueExpr: 'id',
          displayExpr: 'nome',
        },
      },
      {
        dataField: 'cor',
        caption: 'Cor',
        validationRules: [{ type: 'required' }],
        lookup: {
          dataSource: DevExpress.data.AspNet.createStore({
            key: 'id',
            loadUrl: `${url}/Dados/Cor`,
            onBeforeSend(method, ajaxOptions) {
              ajaxOptions.xhrFields = { withCredentials: true };
            },
          }),
          valueExpr: 'id',
          displayExpr: 'nome',
        },
      },
      {
        dataField: 'pessoa',
        caption: 'Pessoa',
        validationRules: [{ type: 'required' }],
        lookup: {
          dataSource: DevExpress.data.AspNet.createStore({
            key: 'id',
            loadUrl: `${url}/Pessoas`,
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
