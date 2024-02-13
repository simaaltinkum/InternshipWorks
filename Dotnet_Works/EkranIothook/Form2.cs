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

        private void button1_Click(object sender, EventArgs e)
        {
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
            HttpRequestMessage request = new HttpRequestMessage();
            request.RequestUri = new Uri("https://iothook.com/api/device/?api_key=1c1094835fe305ad04096223&results=2");
            request.Method = HttpMethod.Get;
            request.Headers.Add("api_key", "1c1094835fe305ad04096223");
            HttpResponseMessage response = await httpClient.SendAsync(request);
            var responseString = await response.Content.ReadAsStringAsync();
            var statusCode = response.StatusCode;

            // string output = JsonConvert.SerializeObject(responseString);
            // MessageBox.Show(responseString);

            dynamic jsonData = JsonConvert.DeserializeObject(responseString);
            string jsonFormatted = JsonConvert.SerializeObject(jsonData, Formatting.Indented);

            // JSON formatına dönüştürülmüş veriyi göster
            MessageBox.Show(jsonFormatted);


            DateTime startDate = new DateTime(2023, 1, 1);
            DateTime endDate = new DateTime(2023, 1, 31);

        }
    }
}
