module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('account',{
        account_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
          },
        email: {
            type: DataTypes.STRING
        },
        password: {
            type: DataTypes.STRING
        }
    });
}