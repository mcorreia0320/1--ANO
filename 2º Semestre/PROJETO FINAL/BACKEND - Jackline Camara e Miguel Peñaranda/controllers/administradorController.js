const { Account, User } = require('../sequelize');

exports.getInfoUsers = function(req, res) {
    Account.findAll({
        include:[{
            model: User,
            attributes: ['firstName', 'lastName', 'born_date']
        }],
        attributes : ['email']
    }).then(users =>{
        res.status(200).json(users);
    }).catch(err =>{
        res.status(500).json(err);
    })
}

exports.DeleteAccount = function(req, res) {
    var email = req.body.email;

    Account.findOne({where:{'email': email}}).then(user =>{
        if (user != null) {
            Account.destroy({where:{'email': email}})
            .then( () =>{
                res.status(200).json({message: 'Conta eliminada com sucesso!'});
            }).catch(err => {res.status(500).json(err);})
        } else res.status(404).json({message: 'Não existe nenhum usuario registado com esse email!'});
    })
}