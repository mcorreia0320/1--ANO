module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('transport',{
        transport_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        type_transport: {
            type: DataTypes.STRING
        }
    });
}