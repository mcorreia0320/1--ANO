const { Account, User, Historial, UserHome, GasConsumption, ElectricityConsumption, FeedingHabits, Diet, UserTransport, Transport } = require('../sequelize');
const { generateAccessToken } = require('../jwtFunctions');

exports.signup = function (req, res) {
    var { email } = req.body;
    var { password } = req.body;

    Account.findOne({
        where: {
            email: email
        }
    }).then(result => {
        if (result == null) {
            if (email.includes('.com') == false){
                res.status(400).json({message: 'O email introduzido não valido'});
            }
            else if (password.length < 6) {
                res.status(400).json({message: 'A palavra-passe deve ter no minimo 6 caracteres!'});
            }
            else { 
                Account.create({ 'email': email, 'password': password })
                .then(user => {                    
                    var token = generateAccessToken(email, password);
                    res.status(200).json({ user, token });                 
                }); 
            }
        }
        else {
            res.status(401).json({message: 'O email inserido já se encontra em uso!'}); 
        }
    }).catch(function (err) {
        // handle error;
        res.status(400).json({message: err}); 
    });
}

exports.createProfile = function(req, res) {
    var {firstname, lastname, bornDate} = req.body;
    var id = req.headers['user-id'];

    User.create({'firstName': firstname, 'lastName': lastname, 'born_date': bornDate, 'accountAccountId': id})
    .then( () =>{
        res.status(200).json({message: 'Perfil do usuario criado com sucesso!'})
    }).catch(err =>{
        res.status(400).json({message: err});
    })
}

exports.updateProfile = function(req, res) {
    var {firstname, lastname, bornDate} = req.body;
    var id = req.headers['user-id'];

    User.update({'firstName': firstname, 'lastName': lastname, 'born_date': bornDate}, {where:{'accountAccountId': id}})
    .then( () =>{
        res.status(200).json({message: 'Perfil do usuario atualizado com sucesso!'})
    }).catch(err =>{
        res.status(400).json({message: err});
    })
}

exports.login = function (req, res) {
    
    var { email, password } = req.body;
    
    if (email.includes('.com') == false){
        res.status(400).json({message: 'O email introduzido não valido'});
    }
    else {
        Account.findOne({
            where: {
                email: email
            }
        }).then(user => {
            if (user == null) {
                res.status(401).json({message: 'O email inserido não se encontra registado!'}); 
            }
            else if (password.length < 6){
                res.status(401).json({message: 'Palavra-passe não valida!'}); 
            }
            else if (user.password != password) {            
                res.status(401).json({message: 'Palavra-passe Incorreta!'}); 
            } else {
                const token = generateAccessToken(email, password);      
                res.status(200).json({ user, token });     
            }
        }).catch(function (err) {
            // handle error;
            res.send(err);
        });
    }

}

exports.updatePassword = function (req, res) {
    var {oldPassword ,newPassword} = req.body;
    var id = req.headers['user-id'];

    Account.findByPk(id).then(user =>{
        if (oldPassword.length < 6){
            res.status(401).json({message: 'Palavra-passe invalida'}); 
        }
        else if (newPassword.length < 6) {
            res.status(401).json({message: 'A palavra-passe deve ter no minimo 6 caracteres!'}); 
        }
        else if (user.password != oldPassword){
            res.status(401).json({message: 'Palavra-passe antiga errada!'}); 
        }
        else if (user.password == newPassword) {
            res.status(401).json({message: 'A palavra-passe deve ser diferente á antiga!'}); 
        }
        else {
            Account.update({'password': newPassword}, {where: {account_id: id}}).then(result =>{
                if (result == 0) {
                    res.status(500).json({message: 'Oops! Algo ocorreu mal...'});
                }
                else {
                    res.status(200).json({message: 'Palavra-passe atualizada com sucesso!'});
                }
            })
        }
    })
}

exports.getProfileUser =  function(req, res) {
    var id = req.headers['user-id'];

    Account.findByPk(id, {include:[
        {model: User,
        include:[{model: UserHome, include:[ GasConsumption, ElectricityConsumption]},
                 {model: FeedingHabits, include:[Diet]},
                 {model: UserTransport, include:[Transport]}]},
        Historial
    ]}).then( user =>{
        if (user == null) {
            res.status(404).json({message: 'Não se encontra nenhuma conta logeada!'});
        }
        else res.status(200).json({user});
    }).catch(function (err) {
        // handle error;
        res.status(400).json({message: err}); 
    });
}

exports.getHistorialUser = (req,res) =>{
    var id = req.headers['user-id'];

    Historial.findAll({where:{'accountAccountId': id}}).then(result =>{
        res.status(200).json({result});
    })
}