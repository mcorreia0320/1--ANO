module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('user',{
        user_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
          },
        firstName: {
            type: DataTypes.STRING
        },
        lastName: {
            type: DataTypes.STRING
        },
        born_date: {
            type: DataTypes.DATE
        }
    });
}