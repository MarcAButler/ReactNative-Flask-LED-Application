import React from 'react'
import { View, Button, Text } from 'react-native'



const ButtonUI = (props) =>
{
    const { name, slug } = props

    const ledON = async () =>
    {
        try
        {
            let response = await fetch(`http://10.14.25.25:5000${slug}`)
            response = await response.text()
            console.log(response)
        }
        catch (error)
        {
            console.error(error)
        }
        
    }

    return(
        <View>
            <Button title={name} onPress={ledON}/>
            <Text>
                {"\n"}
            </Text>
        </View>
    )
}



export default ButtonUI