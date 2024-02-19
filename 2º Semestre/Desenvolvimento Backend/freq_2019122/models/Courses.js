module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('courses',{
        course_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        course_name: {
            type: DataTypes.STRING
        },
        instructor: {
            type: DataTypes.STRING
        }
    });
}