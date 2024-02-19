module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('rentals', {
        rental_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        car_brand: {
            type: DataTypes.STRING
        },
        car_model: {
            type: DataTypes.STRING
        },
        pickup_date: {
            type: DataTypes.DATE
        },
        return_date: {
            type: DataTypes.DATE
        }
    })
}