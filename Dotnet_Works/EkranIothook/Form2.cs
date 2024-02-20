using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;
using System.Xml.Linq;

namespace EkranIothook
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private async void button1_Click(object sender, EventArgs e)
        {

            // DateTime startDate;
            // DateTime endDate;

            string startDate = textBox1.Text;
            string endDate = textBox2.Text;
            string apiKey = "1c1094835fe305ad04096223";

            string apiUrl = $"https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223";

            using (HttpClient httpClient = new HttpClient())
            {
                try
                {
                    HttpResponseMessage response = await httpClient.GetAsync(apiUrl);

                    if (response.IsSuccessStatusCode)
                    {
                        string responseData = await response.Content.ReadAsStringAsync();

                        MessageBox.Show(responseData);
                    }
                    else
                    {
                        MessageBox.Show("HTTP Error: " + response.StatusCode);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error: " + ex.Message);
                }
            }



            Form3 fm3 = new Form3();
            fm3.Show();

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private async void Form2_Load(object sender, EventArgs e)
        {
            HttpClient httpClient = new HttpClient();

            // HttpRequestMessage oluşturulması
            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=1");
            request.Headers.Add("api_key", "1c1094835fe305ad04096223");

            HttpResponseMessage response = await httpClient.SendAsync(request);

            var responseString = await response.Content.ReadAsStringAsync();
            var statusCode = response.StatusCode;

            responseString = responseString.Replace("[", "").Replace("]", "");

            IothookMember member = JsonConvert.DeserializeObject<IothookMember>(responseString);
            string field_4 = member.field_4;
            string field_5 = member.field_5;
            string field_6 = member.field_6;

            MessageBox.Show("Kırmızı: " + field_4 + " Yeşil: " + field_5 + " Sarı: " + field_6);
            
            // JSON formatına dönüştürülmüş veriyi göster
            //  MessageBox.Show(responseString);
        }

        public class IothookMember
        {
            public string field_4 { get; set; }
            public string field_5 { get; set; }
            public string field_6 { get; set; }
        }

        public class Program
        {
            public static async Task Main()
            {
                HttpClient httpClient = new HttpClient();

                // HttpRequestMessage oluşturulması
                HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=2");
                request.Headers.Add("api_key", "1c1094835fe305ad04096223");

                HttpResponseMessage response = await httpClient.SendAsync(request);

                string responseString = await response.Content.ReadAsStringAsync();
                var statusCode = response.StatusCode;

            //     MessageBox.Show(responseString);

                // string jsonString = "{\"Name\":\"John Doe\",\"Bio\":\"Software developer\",\"JoinDate\":\"2023-05-31T20:29:33-04:00\",\"Author\":true}";
                // IothookMember member = JsonSerializer.Deserialize<IothookMember>(jsonString);


            //     Console.WriteLine($"Field1: {member.Field1}");
               // Console.WriteLine($"Field2: {member.Field2}");
               // Console.WriteLine($"Field3: {member.Field3}");
            }
        }
    }
}



