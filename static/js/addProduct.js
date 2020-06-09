// Vue Elements
var app = new Vue({
    el: "#add-form",
    data: {
        nombre: "",
        marca: 0,
        tipo: 0,
        precio: "",
        costo: "",
        stock: "",
        descripcion: "",
    },
    methods: {
        addProduct: function () {
            axios
                .post("/api/add_product", {
                    data: {
                        nombre: this.nombre,
                        marca: this.marca,
                        tipo: this.tipo,
                        precio: this.precio,
                        costo: this.costo,
                        stock: this.stock,
                        descripcion: this.descripcion,
                    }
                })
                .then(function (res) {
                    if (res.status == 200) {

                        setInterval(location.href="/", 3000)
                        
                    }
                })
                .catch(function (err) {
                    console.log(err);
                });
        },
        inicio: function(){
            location.href = '/'
        }
    },
});
